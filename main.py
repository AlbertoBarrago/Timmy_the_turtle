"""
This module is the main entry
"""
import turtle

import timmy


def spyral_demo():
    """
    :return: None
    """
    # Init timmy
    tim_my = timmy.Timmy("turtle", 1, "black")
    # Draw shapes
    tim_my.draw_hirst_painting(100, 20, 50)


if __name__ == "__main__":
    spyral_demo()
# Init screen
SCREEN = turtle.Screen()
SCREEN.exitonclick()
