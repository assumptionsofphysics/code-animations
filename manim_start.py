from manim import *
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(WHITE)
        square2 = Square()
        square2.scale(0.5)
        square2.set_fill(RED, opacity=0.5)
        square2.set_stroke(WHITE)
        
        self.play(Create(square))
        self.play(ReplacementTransform(square, circle))
        self.play(ReplacementTransform(circle, square2))
        self.wait()

