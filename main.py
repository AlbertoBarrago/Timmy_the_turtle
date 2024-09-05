"""
This module is the main entry
"""
import turtle

import timmy


def hirst_paint():
    """
    :return: None
    """
    # Init timmy
    tim_my = timmy.Timmy("turtle", 1, "black")
    # Draw shapes
    tim_my.draw_hirst_painting(100, 20, 50)


if __name__ == "__main__":
    hirst_paint()
# Init screen
SCREEN = turtle.Screen()
SCREEN.exitonclick()
