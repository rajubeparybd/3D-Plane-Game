"""
Landmark structures rendering (Shaheed Minar, Parliament, Radio Tower)
"""
from OpenGL.GL import *
from OpenGL.GLUT import *

from ..game_state import state


def _draw_triangle():
    """Helper to draw a simple triangle shape for parliament cutouts"""
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 1, 0)
    glVertex3f(-0.8, -1, 0)
    glVertex3f(0.8, -1, 0)
    glEnd()


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


def draw_radio_tower(x: float, y: float, z: float, scale: float = 1.0):
    """Draw a radio/communication tower with blinking red lights"""
    glPushMatrix()
    glTranslated(x, y, z)
    glScaled(scale, scale, scale)
    
    # Tower base - concrete foundation
    glColor3f(0.5, 0.5, 0.5)
    glPushMatrix()
    glTranslated(0, 0.1, 0)
    glScaled(0.8, 0.2, 0.8)
    glutSolidCube(1)
    glPopMatrix()
    
    # Main tower structure - lattice frame
    tower_height = 8.0
    tower_width = 0.6
    
    # Four corner posts - red/white pattern
    for dx, dz in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        px = dx * tower_width / 2
        pz = dz * tower_width / 2
        
        # Alternating red and white sections
        section_height = tower_height / 8
        for i in range(8):
            if i % 2 == 0:
                glColor3f(0.9, 0.1, 0.1)  # Red
            else:
                glColor3f(1.0, 1.0, 1.0)  # White
            
            glPushMatrix()
            glTranslated(px * (1 - i * 0.08), 0.2 + section_height * i + section_height / 2, pz * (1 - i * 0.08))
            glScaled(0.08, section_height, 0.08)
            glutSolidCube(1)
            glPopMatrix()
    
    # Cross braces - gray metal
    glColor3f(0.4, 0.4, 0.45)
    for height_level in range(1, 8):
        h = 0.2 + height_level * (tower_height / 8)
        taper = 1 - height_level * 0.08
        hw = tower_width * taper / 2
        
        # Horizontal braces
        for side in range(4):
            glPushMatrix()
            glTranslated(0, h, 0)
            glRotated(side * 90, 0, 1, 0)
            glTranslated(0, 0, hw)
            glScaled(hw * 2, 0.03, 0.03)
            glutSolidCube(1)
            glPopMatrix()
    
    # Top platform
    glColor3f(0.3, 0.3, 0.35)
    glPushMatrix()
    glTranslated(0, tower_height + 0.2, 0)
    glScaled(0.3, 0.05, 0.3)
    glutSolidCube(1)
    glPopMatrix()
    
    # Antenna mast on top
    glColor3f(0.8, 0.8, 0.8)
    glPushMatrix()
    glTranslated(0, tower_height + 0.7, 0)
    glScaled(0.04, 1.0, 0.04)
    glutSolidCube(1)
    glPopMatrix()
    
    # Blinking red lights - using blink_time for animation
    blink_on = (int(state.blink_time * 2) % 2) == 0
    
    glDisable(GL_LIGHTING)
    
    if blink_on:
        # Top light - brightest
        glColor3f(1.0, 0.0, 0.0)
        glPushMatrix()
        glTranslated(0, tower_height + 1.3, 0)
        glutSolidSphere(0.1, 12, 12)
        glPopMatrix()
        
        # Glow effect around top light
        glColor4f(1.0, 0.2, 0.2, 0.4)
        glPushMatrix()
        glTranslated(0, tower_height + 1.3, 0)
        glutSolidSphere(0.2, 12, 12)
        glPopMatrix()
    else:
        # Dim light when off
        glColor3f(0.3, 0.0, 0.0)
        glPushMatrix()
        glTranslated(0, tower_height + 1.3, 0)
        glutSolidSphere(0.08, 10, 10)
        glPopMatrix()
    
    # Middle lights (blink opposite to top)
    mid_blink = not blink_on
    mid_height = tower_height * 0.5
    
    if mid_blink:
        glColor3f(1.0, 0.0, 0.0)
    else:
        glColor3f(0.3, 0.0, 0.0)
    
    for dx, dz in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        glPushMatrix()
        glTranslated(dx * 0.2, mid_height + 0.2, dz * 0.2)
        glutSolidSphere(0.06, 8, 8)
        glPopMatrix()
    
    glEnable(GL_LIGHTING)
    
    glPopMatrix()


def draw_national_parliament(x: float, y: float, z: float, scale: float = 1.0):
    """Draw Bangladesh National Parliament building (Jatiya Sangsad Bhaban)"""
    glPushMatrix()
    glTranslated(x, y, z)
    glScaled(scale, scale, scale)
    
    # Base platform - large concrete foundation
    glColor3f(0.7, 0.68, 0.65)
    glPushMatrix()
    glTranslated(0, 0.15, 0)
    glScaled(8, 0.3, 6)
    glutSolidCube(1)
    glPopMatrix()
    
    # Second level platform
    glColor3f(0.72, 0.7, 0.67)
    glPushMatrix()
    glTranslated(0, 0.4, 0)
    glScaled(7, 0.2, 5)
    glutSolidCube(1)
    glPopMatrix()
    
    # Main building blocks - characteristic geometric brutalist style
    main_color = (0.75, 0.73, 0.7)  # Concrete gray
    
    # Central main hall - cylindrical core
    glColor3f(*main_color)
    glPushMatrix()
    glTranslated(0, 2.5, 0)
    glRotated(-90, 1, 0, 0)
    # Draw octagonal approximation of cylinder using cubes
    for angle in range(0, 360, 45):
        glPushMatrix()
        glRotated(angle, 0, 1, 0)
        glTranslated(1.2, 0, 0)
        glScaled(0.8, 4.0, 1.5)
        glutSolidCube(1)
        glPopMatrix()
    glPopMatrix()
    
    # Corner tower blocks
    tower_positions = [(-2.8, 1.5, -1.8), (2.8, 1.5, -1.8), (-2.8, 1.5, 1.8), (2.8, 1.5, 1.8)]
    
    for tx, ty, tz in tower_positions:
        # Main tower block
        glColor3f(0.73, 0.71, 0.68)
        glPushMatrix()
        glTranslated(tx, ty + 1.0, tz)
        glScaled(1.8, 3.5, 1.5)
        glutSolidCube(1)
        glPopMatrix()
        
        # Circular cutout effect (dark inset)
        glColor3f(0.2, 0.2, 0.22)
        glPushMatrix()
        glTranslated(tx, ty + 1.5, tz + 0.76 * (1 if tz > 0 else -1))
        glScaled(0.8, 1.5, 0.1)
        glutSolidSphere(1, 16, 16)
        glPopMatrix()
        
        # Triangular cutout (geometric pattern)
        glPushMatrix()
        glTranslated(tx + 0.91 * (1 if tx > 0 else -1), ty + 0.8, tz)
        glRotated(90 if tx > 0 else -90, 0, 1, 0)
        glScaled(0.6, 1.2, 0.1)
        _draw_triangle()
        glPopMatrix()
    
    # Side wing buildings
    for side in [-1, 1]:
        glColor3f(0.74, 0.72, 0.69)
        # Long horizontal wings
        glPushMatrix()
        glTranslated(side * 1.5, 1.5, side * 2.5)
        glScaled(3.5, 2.5, 1.2)
        glutSolidCube(1)
        glPopMatrix()
        
        # Window strips (dark horizontal bands)
        glColor3f(0.15, 0.15, 0.18)
        for i in range(3):
            glPushMatrix()
            glTranslated(side * 1.5, 1.0 + i * 0.7, side * 2.5 + side * 0.61)
            glScaled(3.0, 0.15, 0.02)
            glutSolidCube(1)
            glPopMatrix()
    
    # Central dome/roof structure
    glColor3f(0.68, 0.66, 0.63)
    glPushMatrix()
    glTranslated(0, 4.8, 0)
    glScaled(2.5, 0.8, 2.5)
    glutSolidSphere(1, 20, 20)
    glPopMatrix()
    
    # Roof terrace level
    glColor3f(0.7, 0.68, 0.65)
    glPushMatrix()
    glTranslated(0, 4.2, 0)
    glScaled(3.5, 0.15, 3.5)
    glutSolidCube(1)
    glPopMatrix()
    
    # Reflecting pool in front (water)
    glColor3f(0.2, 0.4, 0.6)
    glPushMatrix()
    glTranslated(0, 0.05, 4.5)
    glScaled(6, 0.05, 2)
    glutSolidCube(1)
    glPopMatrix()
    
    # Water shimmer effect
    glDisable(GL_LIGHTING)
    glColor4f(0.4, 0.6, 0.8, 0.3)
    glPushMatrix()
    glTranslated(0, 0.08, 4.5)
    glScaled(5.8, 0.01, 1.8)
    glutSolidCube(1)
    glPopMatrix()
    glEnable(GL_LIGHTING)
    
    glPopMatrix()

