"""
Title: Plane Game 3D
Description: A 3D flight simulator game with plane controls and environment rendering including Shaheed Minar monument
Tags: opengl, glut, 3d-game, flight-simulator, python
Script: Run with `python main.py` after activating virtual environment
"""
import sys

from OpenGL.GL import *
from OpenGL.GLUT import *

from .config import (
    WINDOW_WIDTH, WINDOW_HEIGHT,
    LIGHT_AMBIENT, LIGHT_DIFFUSE, LIGHT_SPECULAR, LIGHT_POSITION,
    MAT_AMBIENT, MAT_DIFFUSE, MAT_SPECULAR, HIGH_SHININESS
)
from .rendering.display import display, resize
from .input.handlers import keyboard_handler, special_key_handler, mouse_handler, idle_handler


def main():
    """Main entry point"""
    glutInit(sys.argv)

    # Center the window on display
    screen_width = glutGet(GLUT_SCREEN_WIDTH)
    screen_height = glutGet(GLUT_SCREEN_HEIGHT)
    window_x = (screen_width - WINDOW_WIDTH) // 2
    window_y = (screen_height - WINDOW_HEIGHT) // 2

    glutInitWindowPosition(window_x, window_y)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGBA)
    
    glutCreateWindow(b"Plane Game 3D")
    
    # Register callbacks
    glutReshapeFunc(resize)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard_handler)
    glutSpecialFunc(special_key_handler)
    glutMouseFunc(mouse_handler)
    glutIdleFunc(idle_handler)
    
    # OpenGL configuration
    glClearColor(0.53, 0.81, 0.92, 1.0)  # Light sky blue fallback
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    
    # Enable blending for sun glow effect
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    
    # Lighting setup
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, LIGHT_AMBIENT)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LIGHT_DIFFUSE)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LIGHT_SPECULAR)
    glLightfv(GL_LIGHT0, GL_POSITION, LIGHT_POSITION)
    
    glMaterialfv(GL_FRONT, GL_AMBIENT, MAT_AMBIENT)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MAT_DIFFUSE)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MAT_SPECULAR)
    glMaterialfv(GL_FRONT, GL_SHININESS, HIGH_SHININESS)
    
    glutMainLoop()


if __name__ == "__main__":
    main()
