"""
Global game state management for Plane Game 3D
"""
import time
import random
from typing import List

from .config import NUM_CLOUDS, NUM_VEHICLES, INITIAL_SPEED


class GameState:
    """Singleton class to manage all game state"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Initialize all game state variables"""
        # Camera/view
        self.zoom = 4.0
        
        # Building data storage
        self.tola = [[0 for _ in range(5000)] for _ in range(5000)]
        
        # Position variables
        self.tX = 0.0
        self.tY = 0.0
        self.tZ = -8.0
        
        # Environment zone positions
        self.tZ1 = -20.0
        self.tZ2 = -40.0
        self.tZ3 = -60.0
        self.tZ4 = -80.0
        self.tZ5 = -100.0
        self.tZ6 = -120.0
        
        # Rotation
        self.rotX = 0.0
        self.rotY = 0.0
        self.rotZ = 0.0
        
        # Game mechanics
        self.speed = INITIAL_SPEED
        self.TIME = 0
        self.SCORE = 0
        
        # Game flags
        self.GAME_OVER = False
        self.START = False
        self.PAUSED = False
        self.rot = False
        
        # Shaheed Minar tracking
        self.shaheed_minar_passed = False
        
        # Obstacle tracking
        self.obstacle_passed = [False, False, False, False, False, False, False]
        
        # Time tracking
        self.start_time = time.time()
        self.pause_start_time = 0.0
        self.total_pause_time = 0.0
        
        # Animation times
        self.glow_time = 0.0
        self.blink_time = 0.0
        
        # Cloud data: [x, y, z, scale]
        self.cloud_data = [
            [random.uniform(-50, 50), random.uniform(18, 50), -10.0 - i * 5.0, random.uniform(1.5, 6.0)]
            for i in range(NUM_CLOUDS)
        ]
        
        # Vehicle data: [x, z, direction, speed, color_idx, color]
        self.vehicle_data: List[List[float]] = []
        
        # Tree positions: [x, y, z, scale]
        self.tree_positions: List[List[float]] = []
        self.TREES_GENERATED = False
    
    def reset(self):
        """Reset game to initial state"""
        self.tX = 0.0
        self.tY = 0.0
        self.tZ = -8.0
        
        self.tZ1 = -20.0
        self.tZ2 = -40.0
        self.tZ3 = -60.0
        self.tZ4 = -80.0
        self.tZ5 = -100.0
        self.tZ6 = -120.0
        
        self.shaheed_minar_passed = False
        
        self.rotX = 0.0
        self.rotY = 0.0
        self.rotZ = 0.0
        
        self.speed = INITIAL_SPEED
        self.TIME = 0
        self.SCORE = 0
        self.GAME_OVER = False
        self.PAUSED = False
        
        self.pause_start_time = 0.0
        self.total_pause_time = 0.0
        
        self.obstacle_passed = [False, False, False, False, False, False, False]
        self.start_time = time.time()
        
        self.glow_time = 0.0
        self.blink_time = 0.0
        
        # Reset vehicles for new random positions
        self.vehicle_data = []
        
        # Reset trees for new random positions
        self.tree_positions = []
        self.TREES_GENERATED = False
        
        # Reset cloud positions with new random values
        self.cloud_data = [
            [random.uniform(-50, 50), random.uniform(18, 50), -10.0 - i * 5.0, random.uniform(1.5, 6.0)]
            for i in range(NUM_CLOUDS)
        ]


# Global state instance
state = GameState()

