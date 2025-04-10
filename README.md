# Manim Environment Setup and Interference Package

## About This Project

This project uses a custom package called **`interference_package`** to simulate and visualize wave interference patterns.

You can import functions like `I1`, `I2`, `Is`, and constants like `c1`, `z`, `l` from `interference_package`.

Example usage inside a Manim scene:

```python
from manim import *
from interference_package import I1, z, l, c1

class SimplePlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-7*z, 7*z, 20],
            y_range=[0, 1, 0.2],
            x_length=10,
            y_length=6,
        )
        plot = axes.plot(lambda x: I1(x, 30*l, c1), color=BLUE)
        self.add(axes, plot)
```

---

## Setting Up the Environment

To get started, clone or download the repository.

It is recommended to create your own virtual environment instead of using the pre-existing `manim_env/` folder.

### Creating a New Virtual Environment

```bash
python -m venv manim_env
```

### Activating the Environment

#### Windows
```bash
.\manim_env\Scripts\activate
```

#### macOS/Linux
```bash
source manim_env/bin/activate
```

Once activated, you'll see `(manim_env)` at the beginning of your command prompt.

---

## Installing Requirements

After activating the environment, install all required Python dependencies:

```bash
pip install -r requirements.txt
```

Make sure you also have a LaTeX distribution installed on your system:
- [TeX Live (Linux/Windows)](https://tug.org/texlive/)
- [MacTeX (Mac)](https://tug.org/mactex/)

LaTeX is needed for Manim to render text labels like axis labels.

---

## Running Manim

After activating the environment and installing requirements, you can run Manim commands as usual.

To run a Manim script:
```bash
manim -pql <filename>.py
```

The flags mean:
- `-p`: Preview the video after rendering
- `-ql`: Low quality (you can use `-qh` for high quality)

To render a specific scene:
```bash
manim -pql <filename>.py SceneName
```

---

## Running Tests

Before running tests, make sure you have installed all requirements including `pytest`.

To run all tests:

```bash
pytest
```

Pytest will automatically discover and run all test cases inside the `tests/` folder.

Example output:
```plaintext
=================================== test session starts ===================================
platform darwin -- Python 3.x.x, pytest-x.x.x
collected 3 items

tests/test_wave_functions.py ...                                             [100%]

==================================== 3 passed in 0.14s ====================================
```

If you prefer, you can also run:

```bash
python -m unittest discover tests
```

---

## Performance Tips

- For development, use `-s` to skip rendering and show the last frame
- Use `-n` to render specific frames only
- First render is usually slowest due to font building and cache generation
- Break complex scenes into smaller parts if needed

---

## First Time Running

- The first time you run Manim, it may take longer due to:
  - Building the font cache
  - Initializing components
  - Compiling and caching animations
- This is normal. Subsequent runs will be faster.
- Some font warnings might appear — these can be safely ignored.

---

## Notes

- Always create and activate your own virtual environment before running Manim commands
- If you get LaTeX errors, double-check that TeX Live (or MacTeX) is properly installed
- For any missing Python packages, reinstall using `pip install -r requirements.txt`
- Avoid uploading your `manim_env/` folder to GitHub; instead, use `requirements.txt` to define dependencies.
