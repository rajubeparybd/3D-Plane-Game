"""
Plane model rendering
"""
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_plane():
    """Draw the airplane model"""
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

