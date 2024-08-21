import random as r
import turtle


class Timmy:
    """
    This class is used to draw shapes and lines.

    :param shape: Shape of the turtle
    :param speed: Speed of the turtle
    :param color: Color of the turtle
    """

    def __init__(self, shape="classic", speed=1, color="black"):
        self.shape = shape
        self.speed = speed
        self.color = color
        self.color_list = ["medium aquamarine", "dark violet", "dark orange", "dark red", "dark green"]

    def init_turtle(self, is_fast=False):
        """
        Initialize the turtle with given attributes.

        :param is_fast: If True, set turtle speed to fastest.
        """
        turtle.shape(self.shape)
        turtle.color(self.color)
        turtle.speed("fastest" if is_fast else self.speed)

    def draw_square(self):
        """Draw a square."""
        self.init_turtle()
        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)

    def draw_circle(self):
        """Draw a circle."""
        self.init_turtle()
        turtle.circle(100)

    def draw_triangle(self):
        """Draw a triangle."""
        self.init_turtle()
        for _ in range(3):
            turtle.forward(100)
            turtle.left(120)

    def draw_star(self):
        """Draw a star."""
        self.init_turtle()
        for _ in range(5):
            turtle.forward(100)
            turtle.left(144)

    def draw_dashed_line(self, length):
        """
        Draw a dashed line.

        :param length: Number of dashes to draw.
        """
        self.init_turtle()
        for _ in range(length):
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()

    def draw_pentagon(self, num_sides):
        """
        Draw a polygon with the specified number of sides.

        :param num_sides: Number of sides for the polygon.
        """
        self.init_turtle()
        angle = 360 / num_sides
        turtle.getscreen().bgcolor("black")
        for _ in range(num_sides):
            turtle.forward(70)
            turtle.right(angle)

    @staticmethod
    def random_color():
        """
        Generate a random color in RGB format.

        :return: A tuple representing the RGB color.
        """
        return r.random(), r.random(), r.random()

    def random_walk(self, num_steps, bg_color):
        """
        Perform a random walk.

        :param num_steps: Number of steps for the random walk.
        :param bg_color: Background color of the turtle screen.
        """
        self.init_turtle(True)
        directions = [0, 90, 180, 270]
        turtle.getscreen().bgcolor(bg_color)
        for _ in range(num_steps):
            turtle.color(self.random_color())
            turtle.forward(30)
            turtle.setheading(r.choice(directions))

    def draw_spirograph(self, gap_size):
        """
        Draw a spirograph with a specific gap size between each rotation.

        :param gap_size: Gap size between rotations.
        """
        self.init_turtle(True)
        for _ in range(int(360 / gap_size)):
            turtle.color(self.random_color())
            turtle.circle(100)
            turtle.setheading(turtle.heading() + gap_size)
