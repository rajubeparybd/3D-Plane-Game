"""
Title: RGBPixmap Module
Description: Handles texture loading and checkerboard pattern generation for OpenGL
Tags: texture, bitmap, opengl, image-processing
"""

import struct
from typing import Tuple
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np


class MRGB:
    """RGB color class with alpha channel"""
    def __init__(self, r: int = 0, g: int = 0, b: int = 0, a: int = 255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a


class RGBPixmap:
    """Handles image loading and texture operations"""
    
    CHECK_IMAGE_WIDTH = 512
    CHECK_IMAGE_HEIGHT = 512
    
    def __init__(self):
        self.n_rows = 0
        self.n_cols = 0
        self.pixels = None
        self.check_image = None
    
    def make_check_image(self) -> np.ndarray:
        """Generate a checkerboard pattern"""
        check_image = np.zeros((self.CHECK_IMAGE_HEIGHT, self.CHECK_IMAGE_WIDTH, 4), dtype=np.uint8)
        
        for i in range(self.CHECK_IMAGE_HEIGHT):
            for j in range(self.CHECK_IMAGE_WIDTH):
                c = (((i & 0x8) == 0) ^ ((j & 0x8) == 0)) * 255
                check_image[i][j] = [c, c, c, 255]
        
        self.check_image = check_image
        return check_image
    
    def make_checker_board(self):
        """Create a checkerboard pattern"""
        self.n_rows = self.n_cols = 64
        self.pixels = []
        
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                c = (((i // 8) + (j // 8)) % 2) * 255
                self.pixels.append(MRGB(c, c, 0, 255))
    
    def set_texture(self, texture_name: int):
        """Set up texture parameters"""
        glBindTexture(GL_TEXTURE_2D, texture_name)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        
        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
        
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        
        if texture_name == 1:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.CHECK_IMAGE_WIDTH, 
                        self.CHECK_IMAGE_HEIGHT, 0, GL_RGBA, GL_UNSIGNED_BYTE, 
                        self.check_image)
        else:
            pixel_data = np.array([[p.r, p.g, p.b, p.a] for p in self.pixels], 
                                 dtype=np.uint8).reshape(self.n_rows, self.n_cols, 4)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.n_cols, self.n_rows, 
                        0, GL_RGBA, GL_UNSIGNED_BYTE, pixel_data)
        
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)
    
    def read_bmp_file(self, filename: str) -> bool:
        """Read a BMP file"""
        try:
            with open(filename, 'rb') as f:
                # Read BMP header
                header = f.read(2)
                if header != b'BM':
                    print(f"Not a valid BMP file: {filename}")
                    return False
                
                # Read file size
                file_size = struct.unpack('<I', f.read(4))[0]
                # Skip reserved fields
                f.read(4)
                # Read offset to pixel data
                off_bits = struct.unpack('<I', f.read(4))[0]
                
                # Read DIB header
                header_size = struct.unpack('<I', f.read(4))[0]
                num_cols = struct.unpack('<I', f.read(4))[0]
                num_rows = struct.unpack('<I', f.read(4))[0]
                planes = struct.unpack('<H', f.read(2))[0]
                bits_per_pixel = struct.unpack('<H', f.read(2))[0]
                compression = struct.unpack('<I', f.read(4))[0]
                image_size = struct.unpack('<I', f.read(4))[0]
                x_pels = struct.unpack('<I', f.read(4))[0]
                y_pels = struct.unpack('<I', f.read(4))[0]
                num_lut_entries = struct.unpack('<I', f.read(4))[0]
                imp_colors = struct.unpack('<I', f.read(4))[0]
                
                if bits_per_pixel != 24:
                    print(f"Not a 24-bit pixel image or is compressed: {filename}")
                    return False
                
                # Calculate padding
                n_bytes_in_row = ((3 * num_cols + 3) // 4) * 4
                num_pad_bytes = n_bytes_in_row - 3 * num_cols
                
                self.n_rows = num_rows
                self.n_cols = num_cols
                self.pixels = []
                
                # Read pixel data
                for row in range(num_rows):
                    for col in range(num_cols):
                        b, g, r = struct.unpack('BBB', f.read(3))
                        self.pixels.append(MRGB(r, g, b, 255))
                    # Skip padding bytes
                    f.read(num_pad_bytes)
                
                return True
                
        except Exception as e:
            print(f"Error reading BMP file {filename}: {e}")
            return False

