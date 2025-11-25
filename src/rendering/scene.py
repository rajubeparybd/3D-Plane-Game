"""
Scene drawing functions
"""
import math
import time
import random

from OpenGL.GL import *
from OpenGL.GLUT import *

from ..config import EN_SIZE, TORUS_POS_X, TORUS_POS_Y, ANGLE_BACK_FRAC, MAX_SPEED
from ..game_state import state
from ..models.plane import draw_plane
from ..models.buildings import draw_house
from ..models.landmarks import draw_shaheed_minar, draw_radio_tower, draw_national_parliament
from ..models.environment import (
    draw_roads, draw_vehicles, draw_trees,
    init_vehicles, update_vehicles, generate_tree_positions
)


def check_collision(plane_x: float, plane_y: float, plane_z: float,
                    obs_x: float, obs_y: float, obs_z: float) -> bool:
    """Check if plane collides with obstacle (torus)"""
    dx = plane_x - obs_x
    dy = (plane_y + 1.0) - obs_y
    dz = plane_z - obs_z

    distance = math.sqrt(dx*dx + dy*dy + dz*dz)
    collision_threshold = 1.8

    return distance < collision_threshold


def check_passed_obstacle(obs_z: float, prev_passed: bool) -> bool:
    """Check if obstacle has just passed the plane"""
    if not prev_passed and 0 < obs_z < 3:
        return True
    return prev_passed


def draw_shaheed_minar_env():
    """Draw environment with Shaheed Minar"""
    # Ground
    glColor3d(0, 0.5, 0.1)
    glPushMatrix()
    glTranslated(0, 0, 0)
    glScaled(EN_SIZE * 2, 0.3, EN_SIZE * 2)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-8, -2.7, -5)
    glRotated(65, 0, 1, 0)
    glScaled(2, 2, 2)
    draw_shaheed_minar()
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(8, -2.7, -5)
    glRotated(-65, 0, 1, 0)
    glScaled(2, 2, 2)
    draw_shaheed_minar()
    glPopMatrix()


def draw_environment(n: int):
    """Draw the game environment with buildings and landmarks"""
    # Ground - grass
    glColor3d(0.15, 0.55, 0.15)
    glPushMatrix()
    glTranslated(0, 0, 0)
    glScaled(EN_SIZE * 2, 0.3, EN_SIZE * 2)
    glutSolidCube(1)
    glPopMatrix()
    
    # Draw roads first (under vehicles)
    draw_roads()

    # Obstacle torus (ring to fly through)
    glColor3d(0, 1, 0.1)
    glPushMatrix()
    glTranslated(TORUS_POS_X[n], TORUS_POS_Y[n], 0)
    glScaled(0.3, 0.3, 0.3)
    glutSolidTorus(1, 3, 30, 30)
    glPopMatrix()
    
    # Draw vehicles on roads
    draw_vehicles()
    
    # Draw trees
    draw_trees()
    
    # Add landmarks based on environment zone number
    if n == 1:
        draw_radio_tower(-15, 0.15, -8, 1.2)
        draw_radio_tower(15, 0.15, 6, 1.0)
    elif n == 2:
        draw_radio_tower(-14, 0.15, 5, 1.3)
    elif n == 3:
        draw_national_parliament(-12, 0.15, -6, 0.8)
    elif n == 4:
        draw_radio_tower(14, 0.15, -5, 1.5)
    elif n == 5:
        draw_national_parliament(12, 0.15, 5, 0.7)
        draw_radio_tower(-14, 0.15, -3, 1.0)
    
    # Buildings
    for i in range(-(EN_SIZE // 2) + 1, EN_SIZE // 2, 2):
        for j in range(-(EN_SIZE // 2) + 1, EN_SIZE // 2, 2):
            idx_i = i + (EN_SIZE // 2) + 1
            idx_j = j + (EN_SIZE // 2) + 1
            
            if idx_i >= 5000 or idx_j >= 5000:
                continue
            
            # Skip building placement where landmarks are
            if n == 3 and i < -8 and -8 < j < -2:
                continue
            if n == 5 and i > 8 and 2 < j < 8:
                continue
                
            if state.tola[idx_i][idx_j] != 0:
                glPushMatrix()
                glTranslated(i, 0, j)
                draw_house(state.tola[idx_i][idx_j], i, j)
                glPopMatrix()
            elif not (-5 <= i <= 5):
                state.tola[idx_i][idx_j] = random.randint(1, 5)
                glPushMatrix()
                glTranslated(i, 0, j)
                draw_house(state.tola[idx_i][idx_j], i, j)
                glPopMatrix()


def draw_scene():
    """Main scene drawing function"""
    if state.GAME_OVER:
        return

    t = (time.time() - state.start_time - state.total_pause_time)
    state.TIME = int(t)
    
    # Update animation times
    state.glow_time = t
    state.blink_time = t
    
    # Initialize vehicles and trees if not done
    init_vehicles()
    generate_tree_positions()

    # Plane rotation limits
    if state.rotX > 11:
        state.rotX = 11
    if state.rotX < -11:
        state.rotX = -11
    if state.rotZ > 10:
        state.rotZ = 10
    if state.rotZ < -15:
        state.rotZ = -15
    
    # Update vehicles
    if not state.PAUSED:
        update_vehicles()
    
    # Draw plane
    glPushMatrix()
    glTranslated(0, 1, 0)
    glRotated(90, 0, 1, 0)
    glRotated(5, 0, 0, 1)
    glRotated(state.rotX, 1, 0, 0)
    glRotated(state.rotY, 0, 1, 0)
    glRotated(state.rotZ, 0, 0, 1)
    glScaled(0.4, 0.4, 0.4)
    draw_plane()
    glPopMatrix()
    
    # Movement limits
    if state.tX >= 4.1:
        state.tX = 4.1
    if state.tX <= -4.1:
        state.tX = -4.1
    if state.tY > 0.1:
        state.tY = 0.1
    if state.tY < -15:
        state.tY = -15
    
    # Draw environments
    glPushMatrix()
    glTranslated(state.tX, state.tY, state.tZ)
    draw_environment(2)
    glPopMatrix()
    
    # Only render Shahid Minar if it hasn't passed yet
    if not state.shaheed_minar_passed:
        glPushMatrix()
        glTranslated(state.tX, state.tY, state.tZ1)
        draw_shaheed_minar_env()
        glPopMatrix()
    
    glPushMatrix()
    glTranslated(state.tX, state.tY, state.tZ2)
    draw_environment(3)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(state.tX, state.tY, state.tZ3)
    draw_environment(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(state.tX, state.tY, state.tZ4)
    draw_environment(5)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(state.tX, state.tY, state.tZ5)
    draw_environment(4)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(state.tX, state.tY, state.tZ6)
    draw_environment(2)
    glPopMatrix()
    
    # Skip all game updates when paused
    if state.PAUSED:
        return
    
    # Update z positions
    state.tZ += state.speed
    state.tZ1 += state.speed
    state.tZ2 += state.speed
    state.tZ3 += state.speed
    state.tZ4 += state.speed
    state.tZ5 += state.speed
    state.tZ6 += state.speed
    
    # Reset positions
    if state.tZ >= 20:
        state.tZ = -110
    if state.tZ1 >= 20:
        state.shaheed_minar_passed = True
    if state.tZ2 >= 20:
        state.tZ2 = -110
    if state.tZ3 >= 20:
        state.tZ3 = -110
    if state.tZ4 >= 20:
        state.tZ4 = -110
    if state.tZ5 >= 20:
        state.tZ5 = -110
    if state.tZ6 >= 20:
        state.tZ6 = -110
    
    # Update cloud positions
    for cloud in state.cloud_data:
        cloud[2] += state.speed
        
        if cloud[2] >= 20:
            cloud[0] = random.uniform(-40, 40)
            cloud[1] = random.uniform(20, 45)
            cloud[2] = -130.0
            cloud[3] = random.uniform(2.0, 5.0)
    
    # Rotation damping
    if state.rotX > 0:
        state.rotX -= ANGLE_BACK_FRAC
    if state.rotX < 0:
        state.rotX += ANGLE_BACK_FRAC
    if state.rotY > 0:
        state.rotY -= ANGLE_BACK_FRAC
    if state.rotY < 0:
        state.rotY += ANGLE_BACK_FRAC
    if state.rotZ > 0:
        state.rotZ -= ANGLE_BACK_FRAC
    if state.rotZ < 0:
        state.rotZ += ANGLE_BACK_FRAC
    
    # Increase speed
    state.speed += 0.0002
    if state.speed >= MAX_SPEED:
        state.speed = MAX_SPEED

    # Collision detection and scoring
    obstacle_zones = [
        (2, state.tZ),
        (3, state.tZ2),
        (1, state.tZ3),
        (5, state.tZ4),
        (4, state.tZ5),
        (2, state.tZ6)
    ]

    for idx, (zone_num, zone_z) in enumerate(obstacle_zones):
        if zone_num in [1, 2, 3, 4, 5]:
            obs_world_x = TORUS_POS_X[zone_num] + state.tX
            obs_world_y = TORUS_POS_Y[zone_num] + state.tY
            obs_world_z = zone_z

            plane_world_x = 0
            plane_world_y = 1
            plane_world_z = 0

            if check_collision(plane_world_x, plane_world_y, plane_world_z,
                             obs_world_x, obs_world_y, obs_world_z):
                state.GAME_OVER = True
                return

            if check_passed_obstacle(obs_world_z, state.obstacle_passed[idx]):
                if not state.obstacle_passed[idx]:
                    state.SCORE += 1
                    state.obstacle_passed[idx] = True

    # Reset obstacle_passed flags when obstacles loop back
    if state.tZ <= -110:
        state.obstacle_passed[0] = False
    if state.tZ2 <= -110:
        state.obstacle_passed[1] = False
    if state.tZ3 <= -110:
        state.obstacle_passed[2] = False
    if state.tZ4 <= -110:
        state.obstacle_passed[3] = False
    if state.tZ5 <= -110:
        state.obstacle_passed[4] = False
    if state.tZ6 <= -110:
        state.obstacle_passed[5] = False

