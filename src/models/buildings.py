"""
Building and house rendering
"""
from OpenGL.GL import *
from OpenGL.GLUT import *

from ..config import BUILDING_COLORS_R, BUILDING_COLORS_G, BUILDING_COLORS_B


def draw_single_floor(r_idx: int, g_idx: int, b_idx: int):
    """Draw a single floor of a building"""
    glColor3d(
        BUILDING_COLORS_R[r_idx % 10],
        BUILDING_COLORS_G[g_idx % 10],
        BUILDING_COLORS_B[b_idx % 10]
    )
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


def draw_house(num_floors: int, r_idx: int, g_idx: int):
    """Draw a multi-story building"""
    for i in range(num_floors):
        glPushMatrix()
        glTranslated(0, 0.8 + i, 0)
        draw_single_floor(g_idx, r_idx, i)
        glPopMatrix()

