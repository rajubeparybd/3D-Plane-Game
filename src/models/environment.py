"""
Environment elements rendering (sky, clouds, trees, roads, vehicles)
"""
import math
import random
from typing import List

from OpenGL.GL import *
from OpenGL.GLUT import *

from ..config import EN_SIZE, NUM_VEHICLES
from ..game_state import state


def draw_sky_gradient():
    """Draw a sky gradient background - light cyan at horizon to deep blue at top"""
    glDisable(GL_LIGHTING)
    glDepthMask(GL_FALSE)
    
    glPushMatrix()
    
    glBegin(GL_QUADS)
    
    # Bottom vertices - light cyan (horizon)
    glColor3f(0.53, 0.81, 0.92)
    glVertex3f(-800, -100, -600)
    glVertex3f(800, -100, -600)
    
    # Top vertices - deeper blue (zenith)
    glColor3f(0.25, 0.41, 0.88)
    glVertex3f(800, 600, -600)
    glVertex3f(-800, 600, -600)
    
    glEnd()
    
    glPopMatrix()
    
    glDepthMask(GL_TRUE)
    glEnable(GL_LIGHTING)


def draw_sun_with_glow():
    """Draw a sun with beautiful layered glow effect"""
    glDisable(GL_LIGHTING)
    glDepthMask(GL_FALSE)
    
    sun_x, sun_y, sun_z = 80.0, 120.0, -400.0
    
    # Pulsating glow intensity
    pulse = 0.15 * math.sin(state.glow_time * 2.0) + 1.0
    
    glPushMatrix()
    glTranslated(sun_x, sun_y, sun_z)
    
    # Outer glow layers (largest to smallest for proper blending)
    glow_layers = [
        (45.0 * pulse, 1.0, 0.85, 0.3, 0.03),
        (35.0 * pulse, 1.0, 0.75, 0.2, 0.05),
        (28.0 * pulse, 1.0, 0.65, 0.1, 0.08),
        (22.0 * pulse, 1.0, 0.55, 0.0, 0.12),
        (16.0 * pulse, 1.0, 0.9, 0.4, 0.2),
        (12.0, 1.0, 0.95, 0.7, 0.5),
        (8.0, 1.0, 1.0, 0.9, 0.9),
    ]
    
    for size, r, g, b, a in glow_layers:
        glColor4f(r, g, b, a)
        glutSolidSphere(size, 20, 20)
    
    # Core sun - bright white/yellow
    glColor3f(1.0, 1.0, 0.95)
    glutSolidSphere(6.0, 25, 25)
    
    glPopMatrix()
    
    glDepthMask(GL_TRUE)
    glEnable(GL_LIGHTING)


def draw_single_cloud(x: float, y: float, z: float, scale: float):
    """Draw a single cloud cluster using grouped spheres"""
    glPushMatrix()
    glTranslated(x, y, z)
    glScaled(scale, scale * 0.6, scale)
    
    glColor3f(1.0, 1.0, 1.0)
    
    # Main body
    glutSolidSphere(1.0, 15, 15)
    
    # Left puff
    glPushMatrix()
    glTranslated(-0.8, 0.1, 0)
    glutSolidSphere(0.7, 15, 15)
    glPopMatrix()
    
    # Right puff
    glPushMatrix()
    glTranslated(0.9, 0.15, 0)
    glutSolidSphere(0.75, 15, 15)
    glPopMatrix()
    
    # Top puff
    glPushMatrix()
    glTranslated(0.2, 0.5, 0)
    glutSolidSphere(0.6, 15, 15)
    glPopMatrix()
    
    # Front puff
    glPushMatrix()
    glTranslated(-0.3, 0.0, 0.5)
    glutSolidSphere(0.55, 15, 15)
    glPopMatrix()
    
    # Back puff
    glPushMatrix()
    glTranslated(0.4, 0.2, -0.4)
    glutSolidSphere(0.5, 15, 15)
    glPopMatrix()
    
    glPopMatrix()


def draw_clouds():
    """Draw multiple clouds scattered across the sky"""
    glDisable(GL_LIGHTING)
    
    for cloud in state.cloud_data:
        x, y, z, scale = cloud
        draw_single_cloud(x, y, z, scale)
    
    glEnable(GL_LIGHTING)


def draw_single_tree(x: float, y: float, z: float, scale: float = 1.0):
    """Draw a single tree with trunk and foliage"""
    glPushMatrix()
    glTranslated(x, y, z)
    glScaled(scale, scale, scale)
    
    # Tree trunk - brown
    glColor3f(0.45, 0.25, 0.1)
    glPushMatrix()
    glTranslated(0, 0.4, 0)
    glScaled(0.15, 0.8, 0.15)
    glutSolidCube(1)
    glPopMatrix()
    
    # Foliage layers
    foliage_colors = [
        (0.1, 0.5, 0.15),   # Dark green
        (0.15, 0.6, 0.2),   # Medium green
        (0.2, 0.65, 0.25),  # Light green
    ]
    
    # Bottom foliage layer
    glColor3f(*foliage_colors[0])
    glPushMatrix()
    glTranslated(0, 0.7, 0)
    glRotated(-90, 1, 0, 0)
    glutSolidCone(0.6, 0.8, 12, 4)
    glPopMatrix()
    
    # Middle foliage layer
    glColor3f(*foliage_colors[1])
    glPushMatrix()
    glTranslated(0, 1.1, 0)
    glRotated(-90, 1, 0, 0)
    glutSolidCone(0.5, 0.7, 12, 4)
    glPopMatrix()
    
    # Top foliage layer
    glColor3f(*foliage_colors[2])
    glPushMatrix()
    glTranslated(0, 1.5, 0)
    glRotated(-90, 1, 0, 0)
    glutSolidCone(0.35, 0.6, 12, 4)
    glPopMatrix()
    
    glPopMatrix()


def generate_tree_positions():
    """Generate random tree positions for the environment"""
    if state.TREES_GENERATED:
        return
    
    state.tree_positions = []
    
    # Generate trees around the edges, avoiding the center flight path
    for _ in range(40):
        side = random.choice([-1, 1])
        x = side * random.uniform(6, 18)
        z = random.uniform(-18, 18)
        scale = random.uniform(0.8, 1.5)
        state.tree_positions.append([x, 0.15, z, scale])
    
    state.TREES_GENERATED = True


def draw_trees():
    """Draw all trees in the environment"""
    for tree_data in state.tree_positions:
        x, y, z, scale = tree_data
        draw_single_tree(x, y, z, scale)


def draw_roads():
    """Draw roads in the environment"""
    glColor3f(0.25, 0.25, 0.28)  # Dark gray asphalt
    
    # Main horizontal road
    glPushMatrix()
    glTranslated(0, 0.16, 0)
    glScaled(EN_SIZE * 2, 0.02, 2.0)
    glutSolidCube(1)
    glPopMatrix()
    
    # Road markings - center line (yellow)
    glColor3f(0.9, 0.8, 0.1)
    for i in range(-EN_SIZE, EN_SIZE, 3):
        glPushMatrix()
        glTranslated(i, 0.17, 0)
        glScaled(1.5, 0.01, 0.1)
        glutSolidCube(1)
        glPopMatrix()
    
    # Side roads perpendicular
    glColor3f(0.25, 0.25, 0.28)
    
    # Left side road
    glPushMatrix()
    glTranslated(-10, 0.16, 0)
    glScaled(1.5, 0.02, EN_SIZE * 2)
    glutSolidCube(1)
    glPopMatrix()
    
    # Right side road
    glPushMatrix()
    glTranslated(10, 0.16, 0)
    glScaled(1.5, 0.02, EN_SIZE * 2)
    glutSolidCube(1)
    glPopMatrix()


def init_vehicles():
    """Initialize vehicle positions and properties"""
    if len(state.vehicle_data) > 0:
        return
    
    # Vehicle colors: [R, G, B]
    vehicle_colors = [
        [0.8, 0.1, 0.1],   # Red
        [0.1, 0.1, 0.8],   # Blue
        [0.9, 0.9, 0.1],   # Yellow
        [0.1, 0.7, 0.1],   # Green
        [0.9, 0.5, 0.0],   # Orange
        [0.6, 0.1, 0.6],   # Purple
        [0.2, 0.2, 0.2],   # Dark gray
        [0.9, 0.9, 0.9],   # White
    ]
    
    for i in range(NUM_VEHICLES):
        x_pos = random.uniform(-18, 18)
        speed_val = random.uniform(0.03, 0.08)
        color_idx = random.randint(0, len(vehicle_colors) - 1)
        
        # Alternate vehicles between two lanes
        if i % 2 == 0:
            lane_z = -0.5
            direction = 1
        else:
            lane_z = 0.5
            direction = -1
        
        state.vehicle_data.append([x_pos, lane_z, direction, speed_val, color_idx, vehicle_colors[color_idx]])


def update_vehicles():
    """Update vehicle positions - make them move horizontally along X-axis"""
    for vehicle in state.vehicle_data:
        vehicle[0] += vehicle[2] * vehicle[3]  # x += direction * speed
        
        # Wrap around when reaching edge of road
        if vehicle[0] > 20:
            vehicle[0] = -20
        elif vehicle[0] < -20:
            vehicle[0] = 20


def draw_single_vehicle(x: float, z: float, direction: int, color: List[float]):
    """Draw a single vehicle (simple car shape)"""
    glPushMatrix()
    glTranslated(x, 0.35, z)
    
    # Rotate car to face direction of travel
    if direction > 0:
        glRotated(90, 0, 1, 0)
    else:
        glRotated(-90, 0, 1, 0)
    
    # Car body
    glColor3f(color[0], color[1], color[2])
    glPushMatrix()
    glScaled(0.5, 0.25, 0.8)
    glutSolidCube(1)
    glPopMatrix()
    
    # Car roof/cabin
    glColor3f(color[0] * 0.8, color[1] * 0.8, color[2] * 0.8)
    glPushMatrix()
    glTranslated(0, 0.18, -0.05)
    glScaled(0.4, 0.2, 0.5)
    glutSolidCube(1)
    glPopMatrix()
    
    # Windows (dark)
    glColor3f(0.1, 0.1, 0.15)
    glPushMatrix()
    glTranslated(0.21, 0.18, -0.05)
    glScaled(0.01, 0.15, 0.4)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.21, 0.18, -0.05)
    glScaled(0.01, 0.15, 0.4)
    glutSolidCube(1)
    glPopMatrix()
    
    # Wheels (black)
    glColor3f(0.1, 0.1, 0.1)
    wheel_positions = [(0.2, -0.1, 0.25), (0.2, -0.1, -0.25),
                       (-0.2, -0.1, 0.25), (-0.2, -0.1, -0.25)]
    for wx, wy, wz in wheel_positions:
        glPushMatrix()
        glTranslated(wx, wy, wz)
        glScaled(0.1, 0.1, 0.08)
        glutSolidSphere(1, 8, 8)
        glPopMatrix()
    
    # Headlights (front)
    glColor3f(1.0, 1.0, 0.8)
    glPushMatrix()
    glTranslated(0.15, 0.0, 0.4)
    glScaled(0.08, 0.08, 0.02)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.15, 0.0, 0.4)
    glScaled(0.08, 0.08, 0.02)
    glutSolidCube(1)
    glPopMatrix()
    
    # Taillights (back, red)
    glColor3f(0.9, 0.1, 0.1)
    glPushMatrix()
    glTranslated(0.15, 0.0, -0.4)
    glScaled(0.08, 0.06, 0.02)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.15, 0.0, -0.4)
    glScaled(0.08, 0.06, 0.02)
    glutSolidCube(1)
    glPopMatrix()
    
    glPopMatrix()


def draw_vehicles():
    """Draw all vehicles moving horizontally on the road"""
    for vehicle in state.vehicle_data:
        x, z, direction, _, _, color = vehicle
        draw_single_vehicle(x, z, direction, color)

