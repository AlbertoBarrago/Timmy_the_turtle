"""
This module is the main entry
"""
import turtle

import timmy

# Init timmy
tim_my = timmy.Timmy("turtle", 1, "black")
# Draw shapes
tim_my.draw_spirograph(10)
# Init screen
SCREEN = turtle.Screen()
SCREEN.exitonclick()
