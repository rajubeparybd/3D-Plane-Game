# Plane Game 3D

A Python-based 3D flight simulator featuring realistic plane controls, procedurally generated cityscapes, and the iconic Shaheed Minar (Martyrs' Monument) from Bangladesh. Built with PyOpenGL and GLUT, this game provides an immersive flying experience with progressive difficulty, smooth animations, and cultural heritage elements.

---

## Requirements

- **Python**: 3.8 or higher
- **Operating System**: Linux, or macOS
- **Graphics**: OpenGL-compatible graphics card
- **Memory**: Minimum 512MB RAM
- **Display**: Minimum 1024x768 resolution

---

## Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Running the Game

### Quick Launch
```bash
chmod +x run.sh
./run.sh
```

### Manual Launch

```bash
# Activate virtual environment
source venv/bin/activate

# Launch game
python -m src.main
```

---

## Controls

### Main Menu
| Key | Action |
|-----|--------|
| `G` | Start Game |
| `Q` or `ESC` | Quit Application |

### During Gameplay
| Key | Action |
|-----|--------|
| `W` | Pitch Down (Move Up) |
| `S` | Pitch Up (Move Down) |
| `A` | Bank Left (Move Left) |
| `D` | Bank Right (Move Right) |
| `M` | Return to Main Menu |
| `Z` | Zoom In |
| `Shift+Z` | Zoom Out |
| `R` | Enable Auto-Rotation |
| `T` | Disable Auto-Rotation |
| `Q` or `ESC` | Quit Game |

---

## Technical Architecture

### Project Structure
```
3D-Plane-Game/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # Core game logic (1000+ lines)
│   └── rgbpixmap.py         # Texture handling (139 lines)
├── requirements.txt         # Python dependencies
├── run.sh                   # Linux/macOS launcher
├── README.md                # This documentation
├── STRUCTURE.md             # Project structure details
└── venv/                    # Virtual environment (auto-generated)
```

### Core Modules

#### `src/main.py` - Game Engine
- **Plane Model**: Detailed 3D aircraft with wings, cockpit, tail, and propeller
- **Environment System**: Procedural city generation with buildings and monuments
- **Physics Engine**: Rotation, translation, and stabilization mechanics
- **Rendering Pipeline**: OpenGL display with lighting and depth testing
- **Input Handler**: Keyboard controls with smooth response
- **UI System**: Stroke text rendering for menus and HUD

#### `src/rgbpixmap.py` - Texture Manager
- **BMP Loader**: 24-bit bitmap file reading with padding support
- **Checkerboard Generator**: Procedural texture pattern creation
- **Texture Mapping**: OpenGL texture binding and parameter configuration
- **RGBA Support**: Full alpha channel management

### Performance Optimizations

1. **Caching**: Building heights cached in 5000x5000 array to prevent regeneration
2. **Culling**: Back-face culling enabled for hidden surface removal
3. **Depth Testing**: GL_LESS depth function for proper 3D ordering
4. **Immediate Mode**: Simplified rendering for rapid prototyping
5. **Speed Capping**: Maximum speed limit prevents performance degradation

### Graphics Configuration

- **Viewport**: 1366x768 default resolution
- **Projection**: Frustum projection with 2.0-1000.0 depth range
- **Lighting**: Single light source with ambient, diffuse, and specular components
- **Materials**: High shininess (100.0) for reflective surfaces
- **Color Mode**: RGB with double buffering

---

## Gameplay Mechanics

### Flight Physics
- **Banking**: Left/right controls produce realistic roll with automatic stabilization
- **Pitching**: Up/down controls adjust altitude with dampening effect
- **Speed**: Progressively increases from 0.3 to 0.7 (max) over flight duration
- **Boundaries**: Movement constrained to X: ±4.1, Y: -15 to 0.1

### Environment Scrolling
- **Six Zones**: Multiple environment sections cycle seamlessly
- **Shaheed Minar Zone**: Special section featuring the monument
- **Building Zones**: Five procedural city sections with varied layouts
- **Loop Points**: Sections reset at Z=20 to Z=-110 for infinite play

### Visual Effects
- **Rotation Damping**: 0.2 units per frame for smooth stabilization
- **Zoom Controls**: Adjustable camera zoom (default: 4.0x)
- **Auto-Rotation**: Optional continuous plane rotation for showcase mode
- **Time Display**: Real-time flight duration counter

---

## License

This educational project is provided as-is for learning purposes. Feel free to modify and extend for educational and non-commercial use.