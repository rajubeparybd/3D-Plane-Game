"""
Title: Plane Game 3D
Description: A 3D flight simulator game with plane controls and environment rendering including Shaheed Minar monument
Tags: opengl, glut, 3d-game, flight-simulator, python
Script: Run with `python main.py` after activating virtual environment
Image Prompts: 
  - Scene 1: Plane flying over city buildings (0-5 seconds)
  - Scene 2: Close-up of Shaheed Minar monument (5-10 seconds)
  - Scene 3: Player controlling plane with WASD keys (10-15 seconds)
  - Scene 4: Aerial view of procedurally generated city (15-20 seconds)
"""

import sys
import time
from typing import List, Tuple
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random

from .rgbpixmap import RGBPixmap


# Constants
RAD = math.pi / 180
EN_SIZE = 20

# Global variables
pix = [RGBPixmap() for _ in range(6)]

zoom = 4.0
tola = [[0 for _ in range(5000)] for _ in range(5000)]
tX, tY, tZ = 0.0, 0.0, -8.0
rX, rY, rZ = 0.0, 0.0, 4.0
tZ1, tZ2, tZ3, tZ4, tZ5, tZ6 = -20.0, -40.0, -60.0, -80.0, -100.0, -120.0
rotX, rotY, rotZ = 0.0, 0.0, 0.0
cosX, cosY, cosZ = 0.0, 1.0, 0.0
angle = 0.0
xEye, yEye, zEye = 0.0, 5.0, 30.0
cenX, cenY, cenZ, roll = 0.0, 0.0, 0.0, 0.0
radius = 0.0
theta, slope = 0.0, 0.0
speed = 0.3
angle_back_frac = 0.2
shaheed_minar_visible = False
r = [0.1, 0.4, 0.0, 0.9, 0.2, 0.5, 0.0, 0.7, 0.5, 0.0]
g = [0.2, 0.0, 0.4, 0.5, 0.2, 0.0, 0.3, 0.9, 0.0, 0.2]
b = [0.4, 0.5, 0.0, 0.7, 0.9, 0.0, 0.1, 0.2, 0.5, 0.0]
TIME = 0
SCORE = 0
GAME_OVER = False
START = False
torus_pos_x = [1.0, -2.0, 3.0, -4.0, -2.0, 0.0, 2.0]
torus_pos_y = [2.0, 3.0, 10.0, 6.0, 7.0, 4.0, 1.0]
obstacle_passed = [False, False, False, False, False, False, False]

rot = False
start_time = time.time()


def resize(width: int, height: int):
    """Handle window resize"""
    ar = width / height if height > 0 else 1.0
    
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 1000.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_shaheed_minar():
    """Draw the Shaheed Minar (Martyrs' Monument)"""
    # Base platforms
    glColor3d(0.4, 0.2, 0.2)
    glPushMatrix()
    glTranslated(0, 1.55, 0)
    glScaled(2, 0.05, 1.5)
    glutSolidCube(1)
    glPopMatrix()
    
    glColor3d(0.4, 0.2, 0.2)
    glPushMatrix()
    glTranslated(0, 1.6, 0)
    glScaled(1.9, 0.05, 1.4)
    glutSolidCube(1)
    glPopMatrix()
    
    glColor3d(0.4, 0.2, 0.2)
    glPushMatrix()
    glTranslated(0, 1.65, 0)
    glScaled(1.8, 0.05, 1.3)
    glutSolidCube(1)
    glPopMatrix()
    
    # Base plate
    glColor3d(1, 1, 1)
    glPushMatrix()
    glTranslated(0, 1.68, -0.4)
    glScaled(0.5, 0.02, 0.08)
    glutSolidCube(1)
    glPopMatrix()
    
    # Main pillar
    glPushMatrix()
    glTranslated(0, 1.99, -0.4)
    glScaled(0.06, 0.7, 0.04)
    glutSolidCube(1)
    glPopMatrix()
    
    # Rods
    glColor3d(0, 0, 0)
    for offset in [0.07, 0.11, 0.15]:
        glPushMatrix()
        glTranslated(offset, 1.99, -0.4)
        glScaled(0.003, 0.7, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.22, 0, 0)
    for offset in [0.07, 0.11, 0.15]:
        glPushMatrix()
        glTranslated(offset, 1.99, -0.4)
        glScaled(0.003, 0.7, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glPopMatrix()
    
    # Horizontal rods
    glPushMatrix()
    glTranslated(2.2, 0, -0.1)
    glScaled(4.2, 1, 1)
    glColor3d(0, 0, 0)
    for y_pos in [1.85, 2.02, 2.18]:
        glPushMatrix()
        glTranslated(-0.528, y_pos, -0.3)
        glScaled(0.1, 0.003, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glColor3d(1, 1, 1)
    glPopMatrix()
    
    # Side pillars
    glColor3d(1, 1, 1)
    glPushMatrix()
    glTranslated(-0.22, 1.99, -0.4)
    glScaled(0.06, 0.7, 0.04)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(0.22, 1.99, -0.4)
    glScaled(0.06, 0.7, 0.04)
    glutSolidCube(1)
    glPopMatrix()
    
    # Upper pillars
    glPushMatrix()
    glTranslated(0, 0.743, -1.424)
    glRotated(45, 1, 0, 0)
    
    glPushMatrix()
    glTranslated(0, 1.99, -0.4)
    glScaled(0.06, 0.3, 0.04)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.22, 1.99, -0.4)
    glScaled(0.06, 0.3, 0.04)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(0.22, 1.99, -0.4)
    glScaled(0.06, 0.3, 0.04)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(0, 2.15, -0.4)
    glScaled(0.5, 0.04, 0.04)
    glutSolidCube(1)
    glPopMatrix()
    
    # Upper rods
    glColor3d(0, 0, 0)
    for offset in [0.07, 0.11, 0.15]:
        glPushMatrix()
        glTranslated(offset, 1.99, -0.4)
        glScaled(0.003, 0.277, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.22, 0, 0)
    for offset in [0.07, 0.11, 0.15]:
        glPushMatrix()
        glTranslated(offset, 1.99, -0.4)
        glScaled(0.003, 0.277, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glPopMatrix()
    
    # Upper horizontal rods
    glPushMatrix()
    glTranslated(2.2, 0, -0.1)
    glScaled(4.2, 1, 1)
    glColor3d(0, 0, 0)
    for y_pos in [1.85, 2.0, 2.15]:
        glPushMatrix()
        glTranslated(-0.528, y_pos, -0.3)
        glScaled(0.1, 0.003, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glColor3d(1, 1, 1)
    glPopMatrix()
    
    glPopMatrix()
    
    # Side angled pillars - Left
    glColor3d(1, 1, 1)
    glPushMatrix()
    glTranslated(0.1, 0, -0.4)
    glRotated(45, 0, 1, 0)
    
    glPushMatrix()
    glTranslated(-0.605, 1.94, -0.3)
    glScaled(0.045, 0.65, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.45, 1.94, -0.3)
    glScaled(0.045, 0.65, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.528, 2.258, -0.3)
    glScaled(0.199, 0.04, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.528, 1.68, -0.3)
    glScaled(0.199, 0.02, 0.06)
    glutSolidCube(1)
    glPopMatrix()
    
    # Rods for left angled pillar
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(-0.64, -0.05, 0.1)
    glScaled(1, 1.02, 1)
    for offset in [0.078, 0.11, 0.145]:
        glPushMatrix()
        glTranslated(offset, 1.99, -0.4)
        glScaled(0.003, 0.56, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glPopMatrix()
    
    # Horizontal rods
    glColor3d(0, 0, 0)
    for y_pos in [1.85, 2.0, 2.15]:
        glPushMatrix()
        glTranslated(-0.528, y_pos, -0.3)
        glScaled(0.1, 0.003, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glColor3d(1, 1, 1)
    
    glPopMatrix()
    
    # Side angled pillars - Right
    glPushMatrix()
    glTranslated(0.65, 0, 0.3)
    glRotated(-45, 0, 1, 0)
    
    glPushMatrix()
    glTranslated(-0.605, 1.94, -0.3)
    glScaled(0.045, 0.65, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.45, 1.94, -0.3)
    glScaled(0.045, 0.65, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.528, 2.258, -0.3)
    glScaled(0.199, 0.04, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.528, 1.68, -0.3)
    glScaled(0.199, 0.02, 0.06)
    glutSolidCube(1)
    glPopMatrix()
    
    # Rods for right angled pillar
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(-0.64, -0.05, 0.1)
    glScaled(1, 1.02, 1)
    for offset in [0.078, 0.11, 0.145]:
        glPushMatrix()
        glTranslated(offset, 1.99, -0.4)
        glScaled(0.003, 0.56, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glPopMatrix()
    glColor3d(1, 1, 1)
    
    # Horizontal rods
    glColor3d(0, 0, 0)
    for y_pos in [1.85, 2.0, 2.15]:
        glPushMatrix()
        glTranslated(-0.528, y_pos, -0.3)
        glScaled(0.1, 0.003, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glColor3d(1, 1, 1)
    
    glPopMatrix()
    
    # Small pillars
    glPushMatrix()
    glTranslated(0.06, 0, 0.14)
    
    # Left small pillar
    glPushMatrix()
    glTranslated(-0.2, 0, -0.31)
    glRotated(45, 0, 1, 0)
    
    glPushMatrix()
    glTranslated(-0.605, 1.88, -0.3)
    glScaled(0.045, 0.4, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.45, 1.88, -0.3)
    glScaled(0.045, 0.4, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.528, 2.08, -0.3)
    glScaled(0.2, 0.04, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.528, 1.68, -0.3)
    glScaled(0.199, 0.02, 0.06)
    glutSolidCube(1)
    glPopMatrix()
    
    # Rods
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(-0.641, 0.43, 0.1)
    glScaled(1, 0.73, 1)
    for offset in [0.078, 0.11, 0.145]:
        glPushMatrix()
        glTranslated(offset, 1.99, -0.4)
        glScaled(0.003, 0.56, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glPopMatrix()
    
    # Horizontal rods
    glColor3d(0, 0, 0)
    for y_pos in [1.8, 1.96]:
        glPushMatrix()
        glTranslated(-0.528, y_pos, -0.3)
        glScaled(0.1, 0.003, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glColor3d(1, 1, 1)
    
    glPopMatrix()
    
    # Right small pillar
    glPushMatrix()
    glTranslated(0.83, 0, 0.39)
    glRotated(-45, 0, 1, 0)
    
    glPushMatrix()
    glTranslated(-0.605, 1.88, -0.3)
    glScaled(0.045, 0.4, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.45, 1.88, -0.3)
    glScaled(0.045, 0.4, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.528, 2.1, -0.3)
    glScaled(0.199, 0.04, 0.03)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-0.528, 1.68, -0.3)
    glScaled(0.199, 0.02, 0.06)
    glutSolidCube(1)
    glPopMatrix()
    
    # Horizontal rods
    glColor3d(0, 0, 0)
    for y_pos in [1.8, 1.96]:
        glPushMatrix()
        glTranslated(-0.528, y_pos, -0.3)
        glScaled(0.1, 0.003, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glColor3d(1, 1, 1)
    
    # Rods
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(-0.641, 0.43, 0.1)
    glScaled(1, 0.73, 1)
    for offset in [0.078, 0.11, 0.145]:
        glPushMatrix()
        glTranslated(offset, 1.99, -0.4)
        glScaled(0.003, 0.56, 0.003)
        glutSolidCube(1)
        glPopMatrix()
    glPopMatrix()
    glColor3d(1, 1, 1)
    
    glPopMatrix()
    
    glPopMatrix()
    
    # Red circle
    glColor3d(1, 0, 0)
    glPushMatrix()
    glTranslated(0, 2.1, -0.44)
    glScaled(0.35, 0.35, 0.01)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()
    
    # Black lines
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(-0.18, 1.9, -0.45)
    glScaled(0.01, 0.5, 0.01)
    glutSolidCube(1)
    glPopMatrix()
    
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(0.18, 1.9, -0.45)
    glScaled(0.01, 0.5, 0.01)
    glutSolidCube(1)
    glPopMatrix()


def fan():
    """Draw a fan/propeller"""
    glColor3d(0.5, 1, 0)
    glPushMatrix()
    glTranslated(0, 0, 0)
    glScaled(1, 1, 0.7)
    glutSolidSphere(0.8, 30, 30)
    glPopMatrix()
    
    glColor3d(0.5, 1, 0)
    glPushMatrix()
    glTranslated(0, 0, 0)
    glRotated(5, 0, 1, 0)
    glScaled(0.5, 2.5, 0.05)
    glutSolidSphere(1, 30, 30)
    glPopMatrix()
    
    glColor3d(0.5, 1, 0)
    glPushMatrix()
    glTranslated(0, 0, 0)
    glRotated(-5, 0, 1, 0)
    glRotated(90, 0, 0, 1)
    glScaled(0.5, 2.5, 0.05)
    glutSolidSphere(1, 30, 30)
    glPopMatrix()


def plane():
    """Draw the airplane"""
    # Main body
    glColor3d(0.5, 1, 0)
    glPushMatrix()
    glTranslated(0, 0, 0)
    glScaled(3, 0.4, 0.5)
    glutSolidSphere(1, 30, 30)
    glPopMatrix()
    
    # Cockpit
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(1.7, 0.1, 0)
    glScaled(1.5, 0.7, 0.8)
    glRotated(40, 0, 1, 0)
    glutSolidSphere(0.45, 30, 30)
    glPopMatrix()
    
    # Right wing
    glColor3d(0.8, 1, 0)
    glPushMatrix()
    glTranslated(0, 0, 1.2)
    glRotated(-50, 0, 1, 0)
    glScaled(0.7, 0.1, 3)
    glRotated(25, 0, 1, 0)
    glutSolidCube(1)
    glPopMatrix()
    
    glColor3d(0.8, 1, 0)
    glPushMatrix()
    glTranslated(-0.3, -0.15, 1.5)
    glRotated(90, 0, 1, 0)
    glScaled(0.1, 0.1, 0.9)
    glutSolidTorus(0.5, 0.5, 50, 50)
    glPopMatrix()
    
    glColor3d(0.8, 1, 0)
    glPushMatrix()
    glTranslated(0.2, -0.15, 0.9)
    glRotated(90, 0, 1, 0)
    glScaled(0.1, 0.1, 0.9)
    glutSolidTorus(0.5, 0.5, 50, 50)
    glPopMatrix()
    
    # Left wing
    glColor3d(0.8, 1, 0)
    glPushMatrix()
    glTranslated(0, 0, -1.2)
    glRotated(50, 0, 1, 0)
    glScaled(0.7, 0.1, 3)
    glRotated(-25, 0, 1, 0)
    glutSolidCube(1)
    glPopMatrix()
    
    glColor3d(0.8, 1, 0)
    glPushMatrix()
    glTranslated(-0.3, -0.15, -1.5)
    glRotated(90, 0, 1, 0)
    glScaled(0.1, 0.1, 0.9)
    glutSolidTorus(0.5, 0.5, 50, 50)
    glPopMatrix()
    
    glColor3d(0.8, 1, 0)
    glPushMatrix()
    glTranslated(0.2, -0.15, -0.9)
    glRotated(90, 0, 1, 0)
    glScaled(0.1, 0.1, 0.9)
    glutSolidTorus(0.5, 0.5, 50, 50)
    glPopMatrix()
    
    # Rear wings
    glPushMatrix()
    glTranslated(-2.8, 0, 0)
    glScaled(0.8, 0.5, 0.3)
    
    # Right rear wing
    glColor3d(0.8, 1, 0)
    glPushMatrix()
    glTranslated(0.4, 0, 1.5)
    glRotated(-30, 0, 1, 0)
    glScaled(0.7, 0.1, 3)
    glRotated(10, 0, 1, 0)
    glutSolidCube(1)
    glPopMatrix()
    
    # Left rear wing
    glColor3d(0.8, 1, 0)
    glPushMatrix()
    glTranslated(0.4, 0, -1.5)
    glRotated(30, 0, 1, 0)
    glScaled(0.7, 0.1, 3)
    glRotated(-10, 0, 1, 0)
    glutSolidCube(1)
    glPopMatrix()
    
    glPopMatrix()
    
    # Rear vertical wing
    glColor3d(0.8, 1, 0)
    glPushMatrix()
    glTranslated(-2.7, 0.5, 0)
    glRotated(45, 0, 0, 1)
    glScaled(0.8, 2, 0.1)
    glRotated(-20, 0, 0, 1)
    glutSolidCube(0.5)
    glPopMatrix()


def single_tola_house(R: int, G: int, B: int):
    """Draw a single floor of a building"""
    glColor3d(r[R % 10], g[G % 10], b[B % 10])
    glPushMatrix()
    glTranslated(0, 0, 0)
    glutSolidCube(1)
    glPopMatrix()
    
    # Windows
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(0.2, 0, 0)
    glScaled(0.3, 0.3, 1.001)
    glutSolidCube(1)
    glPopMatrix()
    
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(-0.2, 0, 0)
    glScaled(0.3, 0.3, 1.001)
    glutSolidCube(1)
    glPopMatrix()
    
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(0, 0, 0.2)
    glScaled(1.001, 0.3, 0.3)
    glutSolidCube(1)
    glPopMatrix()
    
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslated(0, 0, -0.2)
    glScaled(1.001, 0.3, 0.3)
    glutSolidCube(1)
    glPopMatrix()


def house(n: int, R: int, G: int):
    """Draw a multi-story building"""
    for i in range(n):
        glPushMatrix()
        glTranslated(0, 0.8 + i, 0)
        single_tola_house(G, R, i)
        glPopMatrix()


def shaheed_minar_env():
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


def check_collision(plane_x: float, plane_y: float, plane_z: float,
                     obs_x: float, obs_y: float, obs_z: float) -> bool:
    """Check if plane collides with obstacle (torus)"""
    # Calculate distance between plane center and obstacle center
    dx = plane_x - obs_x
    dy = (plane_y + 1.0) - obs_y  # plane_y + 1.0 accounts for plane's Y offset
    dz = plane_z - obs_z

    distance = math.sqrt(dx*dx + dy*dy + dz*dz)

    # Torus outer radius is approximately 1.2 units (3 * 0.3 scale + inner radius)
    # Plane has approximate radius of 1.2 units
    collision_threshold = 1.8

    return distance < collision_threshold


def check_passed_obstacle(obs_z: float, prev_passed: bool) -> bool:
    """Check if obstacle has just passed the plane"""
    # Obstacle passes the plane when it moves from behind (negative z) to in front (positive z)
    # The plane is at z=0 in world space, obstacles move forward (z increases)
    # Count as passed when obstacle is in the narrow zone just after passing (0 < obs_z < 3)
    if not prev_passed and 0 < obs_z < 3:
        return True
    return prev_passed


def environment(n: int):
    """Draw the game environment with buildings"""
    global tola

    # Ground
    glColor3d(0, 0.5, 0.1)
    glPushMatrix()
    glTranslated(0, 0, 0)
    glScaled(EN_SIZE * 2, 0.3, EN_SIZE * 2)
    glutSolidCube(1)
    glPopMatrix()

    # Obstacle torus (ring to fly through)
    glColor3d(0, 1, 0.1)
    glPushMatrix()
    glTranslated(torus_pos_x[n], torus_pos_y[n], 0)
    glScaled(0.3, 0.3, 0.3)
    glutSolidTorus(1, 3, 30, 30)
    glPopMatrix()
    
    # Buildings
    for i in range(-(EN_SIZE // 2) + 1, EN_SIZE // 2, 2):
        for j in range(-(EN_SIZE // 2) + 1, EN_SIZE // 2, 2):
            idx_i = i + (EN_SIZE // 2) + 1
            idx_j = j + (EN_SIZE // 2) + 1
            
            if idx_i >= 5000 or idx_j >= 5000:
                continue
                
            if tola[idx_i][idx_j] != 0:
                glPushMatrix()
                glTranslated(i, 0, j)
                house(tola[idx_i][idx_j], i, j)
                glPopMatrix()
            elif not (-5 <= i <= 5):
                tola[idx_i][idx_j] = random.randint(1, 5)
                glPushMatrix()
                glTranslated(i, 0, j)
                house(tola[idx_i][idx_j], i, j)
                glPopMatrix()


def draw():
    """Main drawing function"""
    global rotX, rotY, rotZ, tX, tY, tZ, tZ1, tZ2, tZ3, tZ4, tZ5, tZ6, speed, TIME
    global SCORE, GAME_OVER, obstacle_passed

    if GAME_OVER:
        return

    t = (time.time() - start_time)
    TIME = int(t)

    # Plane rotation limits
    if rotX > 11:
        rotX = 11
    if rotX < -11:
        rotX = -11
    if rotZ > 10:
        rotZ = 10
    if rotZ < -15:
        rotZ = -15
    
    # Draw plane
    glPushMatrix()
    glTranslated(0, 1, 0)
    glRotated(90, 0, 1, 0)
    glRotated(5, 0, 0, 1)
    glRotated(rotX, 1, 0, 0)
    glRotated(rotY, 0, 1, 0)
    glRotated(rotZ, 0, 0, 1)
    glScaled(0.4, 0.4, 0.4)
    plane()
    glPopMatrix()
    
    # Movement limits
    if tX >= 4.1:
        tX = 4.1
    if tX <= -4.1:
        tX = -4.1
    if tY > 0.1:
        tY = 0.1
    if tY < -15:
        tY = -15
    
    # Draw environments
    glPushMatrix()
    glTranslated(tX, tY, tZ)
    environment(2)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(tX, tY, tZ1)
    shaheed_minar_env()
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(tX, tY, tZ2)
    environment(3)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(tX, tY, tZ3)
    environment(1)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(tX, tY, tZ4)
    environment(5)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(tX, tY, tZ5)
    environment(4)
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(tX, tY, tZ6)
    environment(2)
    glPopMatrix()
    
    # Update z positions
    tZ += speed
    tZ1 += speed
    tZ2 += speed
    tZ3 += speed
    tZ4 += speed
    tZ5 += speed
    tZ6 += speed
    
    # Reset positions
    if tZ >= 20:
        tZ = -110
    if tZ1 >= 20:
        tZ1 = -110
    if tZ2 >= 20:
        tZ2 = -110
    if tZ3 >= 20:
        tZ3 = -110
    if tZ4 >= 20:
        tZ4 = -110
    if tZ5 >= 20:
        tZ5 = -110
    if tZ6 >= 20:
        tZ6 = -110
    
    # Rotation damping
    if rotX > 0:
        rotX -= angle_back_frac
    if rotX < 0:
        rotX += angle_back_frac
    if rotY > 0:
        rotY -= angle_back_frac
    if rotY < 0:
        rotY += angle_back_frac
    if rotZ > 0:
        rotZ -= angle_back_frac
    if rotZ < 0:
        rotZ += angle_back_frac
    
    # Increase speed
    speed += 0.0002
    if speed >= 0.7:
        speed = 0.7

    # Collision detection and scoring for obstacles
    # Map environment zones to their indices: zone 2 (tZ), zone 3 (tZ2), zone 1 (tZ3), zone 5 (tZ4), zone 4 (tZ5), zone 2 (tZ6)
    obstacle_zones = [
        (2, tZ),
        (3, tZ2),
        (1, tZ3),
        (5, tZ4),
        (4, tZ5),
        (2, tZ6)
    ]

    for idx, (zone_num, zone_z) in enumerate(obstacle_zones):
        if zone_num == 2 or zone_num == 3 or zone_num == 1 or zone_num == 5 or zone_num == 4:
            # Calculate obstacle world position
            obs_world_x = torus_pos_x[zone_num] + tX
            obs_world_y = torus_pos_y[zone_num] + tY
            obs_world_z = zone_z

            # Plane is at world position (0, 1, 0) in camera space
            plane_world_x = 0
            plane_world_y = 1
            plane_world_z = 0

            # Check collision
            if check_collision(plane_world_x, plane_world_y, plane_world_z,
                             obs_world_x, obs_world_y, obs_world_z):
                GAME_OVER = True
                return

            # Check if obstacle is passed to increment score
            # obs_world_z is the obstacle's current z position in world space
            if check_passed_obstacle(obs_world_z, obstacle_passed[idx]):
                if not obstacle_passed[idx]:
                    SCORE += 1
                    obstacle_passed[idx] = True

    # Reset obstacle_passed flags when obstacles loop back
    if tZ <= -110:
        obstacle_passed[0] = False
    if tZ2 <= -110:
        obstacle_passed[1] = False
    if tZ3 <= -110:
        obstacle_passed[2] = False
    if tZ4 <= -110:
        obstacle_passed[3] = False
    if tZ5 <= -110:
        obstacle_passed[4] = False
    if tZ6 <= -110:
        obstacle_passed[5] = False


def draw_stroke_text(text: str, x: float, y: float, z: float):
    """Draw stroke text"""
    glPushMatrix()
    glTranslatef(x, y + 8, z)
    glScalef(0.002, 0.002, z)
    
    for char in text:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(char))
    
    glPopMatrix()


def draw_stroke_text2(text: str, x: float, y: float, z: float):
    """Draw larger stroke text"""
    glPushMatrix()
    glTranslatef(x, y + 8, z)
    glScalef(0.005, 0.005, z)
    
    for char in text:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(char))
    
    glPopMatrix()


def draw_stroke_char(char: str, x: float, y: float, z: float):
    """Draw a single stroke character"""
    glPushMatrix()
    glTranslatef(x, y + 8, z)
    glScalef(0.002, 0.002, z)
    glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(char))
    glPopMatrix()


def display():
    """Display callback function"""
    global angle

    t = (time.time() - start_time)
    a = t * 90.0
    aa = a

    if not rot:
        a = 0

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(0.0, 4.5, 10.0,
              0, 4, 0,
              0, 1.0, 0.0)

    if GAME_OVER:
        # Display game over screen
        glPushMatrix()
        glTranslated(0, 2, 0)
        glRotated(aa, 0, 1, 0)
        glScaled(1.5, 1.5, 1.5)
        plane()
        glPopMatrix()

        draw_stroke_text2("GAME OVER", -2, -0.5, 0)
        draw_stroke_text("Press G to Restart or M for Main Menu", -3.5, -1.5, 0)

        # Display final score and time
        draw_stroke_text("TIME : ", -1, -2, 0)
        time_val = TIME
        digits = []
        if time_val == 0:
            digits.append(0)
        else:
            while time_val > 0:
                digits.append(time_val % 10)
                time_val //= 10
            digits.reverse()

        tmp = 0.0
        for digit in digits:
            draw_stroke_char(str(digit), 0.0 + tmp, -2, 0)
            tmp += 0.2

        draw_stroke_text("SCORE : ", -1, -2.5, 0)
        score_val = SCORE
        score_digits = []
        if score_val == 0:
            score_digits.append(0)
        else:
            while score_val > 0:
                score_digits.append(score_val % 10)
                score_val //= 10
            score_digits.reverse()

        tmp = 0.0
        for digit in score_digits:
            draw_stroke_char(str(digit), 0.3 + tmp, -2.5, 0)
            tmp += 0.2

    elif START:
        glPushMatrix()
        glTranslated(0, 0, 0)
        glScaled(zoom, zoom, zoom)
        glRotated(a, 0, 1, 0)
        draw()
        glPopMatrix()
        
        draw_stroke_text("ARROW KEYS: Move Plane, +/- or Mouse Wheel: Zoom, MAIN MENU: M", -8, 0.9, 0)
        draw_stroke_text("TIME : ", 3, 0, 0)

        # Draw time digits
        time_val = TIME
        digits = []
        if time_val == 0:
            digits.append(0)
        else:
            while time_val > 0:
                digits.append(time_val % 10)
                time_val //= 10
            digits.reverse()  # Reverse to show correct order

        tmp = 0.0
        for digit in digits:
            draw_stroke_char(str(digit), 4 + tmp, 0, 0)
            tmp += 0.2

        # Draw score below time
        draw_stroke_text("SCORE : ", 3, -0.5, 0)

        # Draw score digits
        score_val = SCORE
        score_digits = []
        if score_val == 0:
            score_digits.append(0)
        else:
            while score_val > 0:
                score_digits.append(score_val % 10)
                score_val //= 10
            score_digits.reverse()  # Reverse to show correct order

        tmp = 0.0
        for digit in score_digits:
            draw_stroke_char(str(digit), 4.3 + tmp, -0.5, 0)
            tmp += 0.2
    else:
        glPushMatrix()
        glTranslated(0, 3, 0)
        glRotated(aa, 0, 1, 0)
        glScaled(1.5, 1.5, 1.5)
        plane()
        glPopMatrix()
        
        draw_stroke_text("Press G to Start", -1, -1, 0)
        draw_stroke_text2("Plane Game", -2, 0, 0)
    
    glutSwapBuffers()


def reset_game():
    """Reset all game variables"""
    global tX, tY, tZ, tZ1, tZ2, tZ3, tZ4, tZ5, tZ6
    global rotX, rotY, rotZ, speed, TIME, SCORE, GAME_OVER, obstacle_passed, start_time

    tX, tY, tZ = 0.0, 0.0, -8.0
    tZ1, tZ2, tZ3, tZ4, tZ5, tZ6 = -20.0, -40.0, -60.0, -80.0, -100.0, -120.0
    rotX, rotY, rotZ = 0.0, 0.0, 0.0
    speed = 0.3
    TIME = 0
    SCORE = 0
    GAME_OVER = False
    obstacle_passed = [False, False, False, False, False, False, False]
    start_time = time.time()


def key(key_char: bytes, x: int, y: int):
    """Keyboard callback function"""
    global zoom, tY, tX, rotX, rotY, rotZ, START, rot

    key_str = key_char.decode('utf-8')
    frac = 0.3
    rot_frac = 1.0

    if key_str == '\x1b' or key_str == 'q':  # ESC or 'q'
        sys.exit(0)
    elif key_str == 'r':
        rot = True
    elif key_str == 't':
        rot = False
    elif key_str == '+' or key_str == '=':
        zoom += 0.05
    elif key_str == '-' or key_str == '_':
        zoom -= 0.05
    elif key_str == 'g':
        reset_game()
        START = True
    elif key_str == 'm':
        reset_game()
        START = False

    glutPostRedisplay()


def special_key(key: int, x: int, y: int):
    """Special keyboard callback function for arrow keys"""
    global tY, tX, rotX, rotY, rotZ

    frac = 0.3
    rot_frac = 1.0

    if key == GLUT_KEY_UP:
        tY -= frac
        rotZ += rot_frac
    elif key == GLUT_KEY_DOWN:
        tY += frac
        rotZ -= rot_frac
    elif key == GLUT_KEY_LEFT:
        tX += frac
        rotX -= rot_frac * 3
        rotY += rot_frac / 2
    elif key == GLUT_KEY_RIGHT:
        tX -= frac
        rotX += rot_frac * 3
        rotY -= rot_frac / 2

    glutPostRedisplay()


def mouse_wheel(button: int, direction: int, x: int, y: int):
    """Mouse callback function for zoom control with mouse wheel"""
    global zoom

    if button == 3:  # Scroll up
        zoom += 0.05
    elif button == 4:  # Scroll down
        zoom -= 0.05

    glutPostRedisplay()


def idle():
    """Idle callback function"""
    glutPostRedisplay()


# Light configuration
light_ambient = [0.0, 0.0, 0.0, 1.0]
light_diffuse = [1.0, 1.0, 1.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [2.0, 5.0, 5.0, 0.0]

mat_ambient = [0.7, 0.7, 0.7, 1.0]
mat_diffuse = [0.8, 0.8, 0.8, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
high_shininess = [100.0]


def main():
    """Main entry point"""
    glutInit(sys.argv)

    # Center the window on display
    window_width = 1366
    window_height = 720
    screen_width = glutGet(GLUT_SCREEN_WIDTH)
    screen_height = glutGet(GLUT_SCREEN_HEIGHT)
    window_x = (screen_width - window_width) // 2
    window_y = (screen_height - window_height) // 2

    glutInitWindowPosition(window_x, window_y)
    glutInitWindowSize(window_width, window_height)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGBA)
    
    glutCreateWindow(b"Plane Game 3D")
    
    glutReshapeFunc(resize)
    glutDisplayFunc(display)
    glutKeyboardFunc(key)
    glutSpecialFunc(special_key)
    glutMouseFunc(mouse_wheel)
    glutIdleFunc(idle)
    
    glClearColor(1, 1, 1, 1)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)
    
    glutMainLoop()


if __name__ == "__main__":
    main()

