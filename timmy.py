"""
This module contains the Timmy class, which provides various drawing functionalities using the turtle module.
It includes methods for drawing shapes, random walks, and spirographs.
"""

import random as r
from turtle import Turtle

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
        t = Turtle()
        t.shape(self.shape)
        t.color(self.color)
        t.speed("fastest" if is_fast else self.speed)
        return t

    def draw_square(self):
        """Draw a square."""
        t = self.init_turtle()
        for _ in range(4):
            t.forward(100)
            t.left(90)

    def draw_circle(self):
        """Draw a circle."""
        t = self.init_turtle()
        t.circle(100)

    def draw_triangle(self):
        """Draw a triangle."""
        t = self.init_turtle()
        for _ in range(3):
            t.forward(100)
            t.left(120)

    def draw_star(self):
        """Draw a star."""
        t = self.init_turtle()
        for _ in range(5):
            t.forward(100)
            t.left(144)

    def draw_dashed_line(self, length):
        """
        Draw a dashed line.

        :param length: Number of dashes to draw.
        """
        t = self.init_turtle()
        for _ in range(length):
            t.forward(10)
            t.penup()
            t.forward(10)
            t.pendown()

    def draw_pentagon(self, num_sides):
        """
        Draw a polygon with the specified number of sides.

        :param num_sides: Number of sides for the polygon.
        """
        t = self.init_turtle()
        angle = 360 / num_sides
        t.getscreen().bgcolor("black")
        for _ in range(num_sides):
            t.forward(70)
            t.right(angle)

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
        t = self.init_turtle(True)
        directions = [0, 90, 180, 270]
        t.getscreen().bgcolor(bg_color)
        for _ in range(num_steps):
            t.color(self.random_color())
            t.forward(30)
            t.setheading(r.choice(directions))

    def draw_spirograph(self, gap_size):
        """
        Draw a spirograph with a specific gap size between each rotation.

        :param gap_size: Gap size between rotations.
        """
        t = self.init_turtle(True)
        for _ in range(int(360 / gap_size)):
            t.color(self.random_color())
            t.circle(100)
            t.setheading(t.heading() + gap_size)
