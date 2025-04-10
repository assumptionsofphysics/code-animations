from manim import *
from interference_package import I1, I2, Is, c1, z, l, spherical_path, find_c1
import numpy as np

class VaryingDPlot(Scene):
    def construct(self):
        domain = 7 * z
        scale = 7e9
        # Set up axes for plotting
        axes = Axes(
            x_range=[-domain, domain, 20],
            y_range=[0, 1, 0.2],
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="Intensity")

        # Define the range for x values
        x_vals = np.linspace(-10 * z, 10 * z, int(10 * z))

        # Initialize plots for I1, I2, and Is
        d = ValueTracker(30 * l)

        # Define the functions I1, I2, and Is
        I1_plot = always_redraw(lambda: axes.plot(
            lambda x: scale * I1(x, d.get_value(), c1),
            x_range=[-domain, domain],
            color=BLUE
        ))
        I2_plot = always_redraw(lambda: axes.plot(
            lambda x: scale * I2(x, d.get_value(), c1),
            x_range=[-domain, domain],
            color=RED
        ))
        Is_plot = always_redraw(lambda: axes.plot(
            lambda x: scale * Is(x, d.get_value(), c1),
            x_range=[-domain, domain],
            color=GREEN
        ))

        # Add everything to the scene
        self.add(axes, labels, I1_plot, I2_plot, Is_plot)

        # Animate d from 0 * l to 10 * l
        self.play(d.animate.set_value(0), run_time=10, rate_func=linear)

class VaryingCPlot(Scene):
    def construct(self):
        domain = 4.7 * z
        scale = 7e9
        d = 9*l
        # Set up axes for plotting
        axes = Axes(
            x_range=[-domain, domain, 10],
            y_range=[0, 1, 0.2],
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="Intensity")

        # Define the range for x values
        x_vals = np.linspace(-10 * z, 10 * z, int(10 * z))

        # Create a ValueTracker to control time
        time_tracker = ValueTracker(0)


        # Define the functions I1, I2, and Is
        I1_plot = always_redraw(lambda: axes.plot(
            lambda x: scale * I1(x, d, find_c1(spherical_path(time_tracker.get_value()))),
            x_range=[-domain, domain],
            color=BLUE
        ))
        I2_plot = always_redraw(lambda: axes.plot(
            lambda x: scale * I2(x, d, find_c1(spherical_path(time_tracker.get_value()))),
            x_range=[-domain, domain],
            color=RED
        ))
        Is_plot = always_redraw(lambda: axes.plot(
            lambda x: scale * Is(x, d, find_c1(spherical_path(time_tracker.get_value()))),
            x_range=[-domain, domain],
            color=GREEN
        ))


        # Draw C1^2 Variable, update dynamically
        c1_var = Variable(abs(find_c1(spherical_path(0)))**2, 'c_1^2', num_decimal_places=2)
        c1_var.to_edge(LEFT)
        c1_var.add_updater(lambda v: v.tracker.set_value(abs(find_c1(spherical_path(time_tracker.get_value())))**2))

        # Add elements to the scene
        self.add(axes, labels, I1_plot, I2_plot, Is_plot, c1_var)

        # Animate time_tracker from 0 to 1
        self.play(time_tracker.animate.set_value(1), run_time=5*30/30, rate_func=linear)

        self.wait(1)