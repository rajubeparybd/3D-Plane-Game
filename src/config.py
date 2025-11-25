"""
Configuration constants for Plane Game 3D
"""
import math

# Math constants
RAD = math.pi / 180

# Environment size
EN_SIZE = 20

# Building color palettes
BUILDING_COLORS_R = [0.1, 0.4, 0.0, 0.9, 0.2, 0.5, 0.0, 0.7, 0.5, 0.0]
BUILDING_COLORS_G = [0.2, 0.0, 0.4, 0.5, 0.2, 0.0, 0.3, 0.9, 0.0, 0.2]
BUILDING_COLORS_B = [0.4, 0.5, 0.0, 0.7, 0.9, 0.0, 0.1, 0.2, 0.5, 0.0]

# Obstacle positions for each zone
TORUS_POS_X = [1.0, -2.0, 3.0, -4.0, -2.0, 0.0, 2.0]
TORUS_POS_Y = [2.0, 3.0, 10.0, 6.0, 7.0, 4.0, 1.0]

# Cloud configuration
NUM_CLOUDS = 20

# Vehicle configuration
NUM_VEHICLES = 12

# Initial game values
INITIAL_SPEED = 0.3
MAX_SPEED = 0.7
ANGLE_BACK_FRAC = 0.2

# Window configuration
WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 720

# Light configuration
LIGHT_AMBIENT = [0.0, 0.0, 0.0, 1.0]
LIGHT_DIFFUSE = [1.0, 1.0, 1.0, 1.0]
LIGHT_SPECULAR = [1.0, 1.0, 1.0, 1.0]
LIGHT_POSITION = [2.0, 5.0, 5.0, 0.0]

# Material configuration
MAT_AMBIENT = [0.7, 0.7, 0.7, 1.0]
MAT_DIFFUSE = [0.8, 0.8, 0.8, 1.0]
MAT_SPECULAR = [1.0, 1.0, 1.0, 1.0]
HIGH_SHININESS = [100.0]

