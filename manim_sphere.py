from manim import *

class DrawSphere(ThreeDScene):
    def construct(self):
        # Create a 3D axes for reference
        axes = ThreeDAxes()

        # Create a sphere object
        sphere = Sphere(radius=2, color=BLUE).set_opacity(0.4)

        # Move the camera to a 3D perspective
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add the axes and sphere to the scene
        self.add(axes, sphere)

        # Animate the sphere by rotating it
        self.play(SpinInFromNothing(sphere))
        self.wait(1)
        self.play(Rotate(sphere, angle=PI, axis=UP))
        self.wait(2)