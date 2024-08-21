import turtle
from timmy import Timmy

#Init timmy
timmy = Timmy("turtle", 1, "black")
#Draw shapes
timmy.do_a_draw_spirograph(10)
#Init screen
screen = turtle.Screen()
screen.exitonclick()
