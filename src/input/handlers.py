"""
Input handling functions (keyboard, mouse)
"""
import sys
import time

from OpenGL.GLUT import *

from ..game_state import state


def keyboard_handler(key_char: bytes, x: int, y: int):
    """Keyboard callback function"""
    key_str = key_char.decode('utf-8')

    if key_str == '\x1b' or key_str == 'q':  # ESC or 'q'
        sys.exit(0)
    elif key_str == ' ':  # Space bar
        if not state.PAUSED:
            state.pause_start_time = time.time()
            state.PAUSED = True
        else:
            state.total_pause_time += time.time() - state.pause_start_time
            state.PAUSED = False
    elif key_str == 'r':
        state.rot = True
    elif key_str == 't':
        state.rot = False
    elif key_str == '+' or key_str == '=':
        state.zoom += 0.05
    elif key_str == '-' or key_str == '_':
        state.zoom -= 0.05
    elif key_str == 'g':
        state.reset()
        state.START = True
    elif key_str == 'm':
        state.reset()
        state.START = False

    glutPostRedisplay()


def special_key_handler(key: int, x: int, y: int):
    """Special keyboard callback function for arrow keys"""
    frac = 0.3
    rot_frac = 1.0

    if key == GLUT_KEY_UP:
        state.tY -= frac
        state.rotZ += rot_frac
    elif key == GLUT_KEY_DOWN:
        state.tY += frac
        state.rotZ -= rot_frac
    elif key == GLUT_KEY_LEFT:
        state.tX += frac
        state.rotX -= rot_frac * 3
        state.rotY += rot_frac / 2
    elif key == GLUT_KEY_RIGHT:
        state.tX -= frac
        state.rotX += rot_frac * 3
        state.rotY -= rot_frac / 2

    glutPostRedisplay()


def mouse_handler(button: int, direction: int, x: int, y: int):
    """Mouse callback function for zoom control with mouse wheel"""
    if button == 3:  # Scroll up
        state.zoom += 0.05
    elif button == 4:  # Scroll down
        state.zoom -= 0.05

    glutPostRedisplay()


def idle_handler():
    """Idle callback function"""
    glutPostRedisplay()

