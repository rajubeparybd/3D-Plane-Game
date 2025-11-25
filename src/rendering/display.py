"""
Main display and window functions
"""
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from ..game_state import state
from ..models.plane import draw_plane
from ..models.environment import draw_sky_gradient, draw_sun_with_glow, draw_clouds
from .text import draw_stroke_text, draw_stroke_text_large, draw_stroke_char
from .scene import draw_scene


def resize(width: int, height: int):
    """Handle window resize"""
    ar = width / height if height > 0 else 1.0
    
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 1000.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    """Display callback function"""
    t = (time.time() - state.start_time)
    a = t * 90.0
    aa = a

    if not state.rot:
        a = 0

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(0.0, 4.5, 10.0,
              0, 4, 0,
              0, 1.0, 0.0)

    # Draw sky elements (background)
    draw_sky_gradient()

    if state.GAME_OVER:
        glPushMatrix()
        glTranslated(0, 2, 0)
        glRotated(aa, 0, 1, 0)
        glScaled(1.5, 1.5, 1.5)
        draw_plane()
        glPopMatrix()

        draw_stroke_text_large("GAME OVER", -2, -0.5, 0)
        draw_stroke_text("Press G to Restart or M for Main Menu", -3.5, -1.5, 0)

        # Display final score and time
        draw_stroke_text("TIME : ", -1, -2, 0)
        time_val = state.TIME
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
        score_val = state.SCORE
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

    elif state.START:
        draw_sky_gradient()
        draw_sun_with_glow()
        draw_clouds()
        glPushMatrix()
        glTranslated(0, 0, 0)
        glScaled(state.zoom, state.zoom, state.zoom)
        glRotated(a, 0, 1, 0)
        draw_scene()
        glPopMatrix()
        
        draw_stroke_text("ARROW KEYS: Move Plane, +/- or Mouse Wheel: Zoom, SPACE: Pause, MAIN MENU: M", -8, 0.9, 0)
        
        # Display PAUSED indicator
        if state.PAUSED:
            draw_stroke_text_large("PAUSED", -1, 2, 0)
        draw_stroke_text("TIME : ", 3, 0, 0)

        # Draw time digits
        time_val = state.TIME
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
            draw_stroke_char(str(digit), 4 + tmp, 0, 0)
            tmp += 0.2

        # Draw score below time
        draw_stroke_text("SCORE : ", 3, -0.5, 0)

        # Draw score digits
        score_val = state.SCORE
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
            draw_stroke_char(str(digit), 4.3 + tmp, -0.5, 0)
            tmp += 0.2
    else:
        glPushMatrix()
        glTranslated(0, 3, 0)
        glRotated(aa, 0, 1, 0)
        glScaled(1.5, 1.5, 1.5)
        draw_plane()
        glPopMatrix()
        
        draw_stroke_text("Press G to Start", -1, -1, 0)
        draw_stroke_text_large("Plane Game", -2, 0, 0)
    
    glutSwapBuffers()

