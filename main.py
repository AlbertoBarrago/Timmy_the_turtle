import random as r
import turtle


def do_a_square():
    turtle.shape("turtle")
    turtle.color("red")
    turtle.speed(.7)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(90)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(90)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(90)
    turtle.speed(.7)
    turtle.forward(100)


# do_a_square()

def do_a_circle():
    turtle.shape("turtle")
    turtle.color("blue")
    turtle.speed(.7)
    turtle.circle(100)


# do_a_circle()


def do_a_triangle():
    turtle.shape("turtle")
    turtle.color("green")
    turtle.speed(.7)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(120)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(120)
    turtle.forward(100)


# do_a_triangle()


def do_a_star():
    turtle.shape("turtle")
    turtle.color("purple")
    turtle.speed(.7)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(144)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(144)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(144)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(144)
    turtle.forward(100)
    turtle.speed(.7)
    turtle.left(144)
    turtle.forward(100)


# do_a_star()

# def dashed_line():
#     for _ in range(6):
#         turtle.penup()
#         turtle.forward(10)
#         turtle.pendown()
#         turtle.forward(10)
#         turtle.penup()
#         turtle.forward(10)
#         turtle.pendown()
#         turtle.forward(10)
#         turtle.penup()
#         turtle.forward(10)
#         turtle.pendown()
#         turtle.forward(10)
#
# turtle.speed(1)
# dashed_line()
# turtle.left(90)
# dashed_line()
# turtle.left(90)
# dashed_line()
# turtle.left(90)
# dashed_line()
# turtle.left(90)

# def drawn_pentagonal(num_sides):
#     angle = 360 / num_sides
#     turtle.getscreen().bgcolor("black")
#     for _ in range(num_sides):
#         turtle.forward(70)
#         turtle.right(angle)
#     for _ in range(num_sides):
#         turtle.forward(70)
#         turtle.left(angle)
#
# for shape_side_n in range(3, 11):
#     turtle.color(random.choice(["medium aquamarine", "dark violet", "dark orange", "dark red", "dark green"]))
#     drawn_pentagonal(shape_side_n)

def random_color():
    rgb_r = r.random()
    rgb_g = r.random()
    rgb_b = r.random()
    rgb_color = (rgb_r, rgb_g, rgb_b)
    return rgb_color
#
# def random_walk(num_steps, bg_color):
#     directions = [0, 90, 180, 270]
#     turtle.getscreen().bgcolor(bg_color)
#     turtle.pensize(7)
#     turtle.speed("fastest")
#     for _ in range(num_steps):
#         turtle.color(random_color())
#         turtle.forward(30)
#         turtle.setheading(r.choice(directions))
#
#
# random_walk(200, "black")

def draw_spirograph(size_of_gap):
    turtle.speed("fastest")
    turtle.shape("turtle")
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(3)

screen = turtle.Screen()
screen.exitonclick()
