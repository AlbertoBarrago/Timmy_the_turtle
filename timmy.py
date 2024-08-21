import random as r
import turtle


class Timmy:
    """
    This class is used to draw shapes and lines.
    :param shape: shape of the turtle
    :param speed: speed of the turtle
    :param color: color of the turtle
    """

    def __init__(self, shape, speed, color):
        self.shape = shape if shape else "classic"
        self.speed = speed if speed else 1
        self.color = color if color else "black"
        self.color_list = ["medium aquamarine", "dark violet", "dark orange", "dark red", "dark green"]

    def init_tutle(self, is_fast=None):
        """
        This method is used to initialize the turtle.
        :param is_fast:
        :return:
        """
        turtle.shape(self.shape)
        turtle.color(self.color)
        turtle.speed("fastest" if is_fast else 1)

    def do_a_square(self):
        """
        This method is used to draw a square.
        :return:
        """
        self.init_tutle()
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)

    def do_a_circle(self):
        """
        This method is used to draw a circle.
        :return:
        """
        self.init_tutle()
        turtle.circle(100)

    def do_a_triangle(self):
        """
        This method is used to draw a triangle.
        :return:
        """
        self.init_tutle()
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)

    def do_a_star(self):
        """
        This method is used to draw a star.
        :return:
        """
        self.init_tutle()
        turtle.forward(100)
        turtle.left(144)
        turtle.forward(100)
        turtle.left(144)
        turtle.forward(100)
        turtle.left(144)
        turtle.forward(100)
        turtle.left(144)
        turtle.forward(100)
        turtle.left(144)
        turtle.forward(100)

    def do_a_dashed_line(self, range_value):
        """
        This method is used to draw a dashed line.
        :param range_value:
        :return:
        """
        self.init_tutle()
        for _ in range(range_value):
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
            turtle.forward(10)

    def do_a_drawn_pentagonal(self, num_sides):
        """
        This method is used to draw a pentagonal.
        :param num_sides:
        :return:
        """
        self.init_tutle()
        angle = 360 / num_sides
        turtle.getscreen().bgcolor("black")
        for _ in range(num_sides):
            turtle.forward(70)
            turtle.right(angle)

    @staticmethod
    def random_color():
        rgb_r = r.random()
        rgb_g = r.random()
        rgb_b = r.random()
        rgb_color = (rgb_r, rgb_g, rgb_b)
        return rgb_color

    def do_a_random_walk(self, num_steps, bg_color):
        """
        This method is used to draw a random walk.
        :param num_steps:
        :param bg_color:
        :return:
        """
        self.init_tutle(True)
        directions = [0, 90, 180, 270]
        turtle.getscreen().bgcolor(bg_color)
        for _ in range(num_steps):
            turtle.color(self.random_color())
            turtle.forward(30)
            turtle.setheading(r.choice(directions))

    def do_a_draw_spirograph(self, size_of_gap):
        """
        This method is used to draw a spirograph.
        :param size_of_gap:
        :return:
        """
        self.init_tutle(True)
        for _ in range(int(360 / size_of_gap)):
            turtle.color(self.random_color())
            turtle.circle(100)
            turtle.setheading(turtle.heading() + size_of_gap)
