"""
Turtle Race
"""
from turtle import Turtle, Screen
import random as r

IS_RACE_ON = False
SCREEN = Screen()
SCREEN.setup(width=500, height=400)
user_bet = SCREEN.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
y_position = [-70, -40, -10, 20, 50, 80]
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

for _ in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[_])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[_])
    turtle_list.append(new_turtle)

if user_bet:
    IS_RACE_ON = True

while IS_RACE_ON:
    for turtle in turtle_list:
        turtle.forward(r.randint(0, 10))
        if turtle.xcor() > 230:
            IS_RACE_ON = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

SCREEN.exitonclick()
