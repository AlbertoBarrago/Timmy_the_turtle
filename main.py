"""
This module is the main entry
"""
import turtle
from timmy import Timmy

#Init timmy
timmy = Timmy("turtle", 1, "black")
#Draw shapes
timmy.random_walk(190, "black")
#Init screen
SCREEN = turtle.Screen()
SCREEN.exitonclick()
