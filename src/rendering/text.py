"""
Text rendering utilities
"""
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_stroke_text(text: str, x: float, y: float, z: float):
    """Draw stroke text at normal size"""
    glPushMatrix()
    glTranslatef(x, y + 8, z)
    glScalef(0.002, 0.002, z)
    
    for char in text:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(char))
    
    glPopMatrix()


def draw_stroke_text_large(text: str, x: float, y: float, z: float):
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

