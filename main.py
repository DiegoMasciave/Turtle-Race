import turtle
from turtle import Turtle, Screen

#********************************DRAW WITH TURTLE************************************************
#
#
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def counter_clockwise():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def clockwise():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(counter_clockwise, "a")
# screen.onkey(clockwise, "d")
# screen.onkey(clear, "c")
#
#********************************RACE TURTLE************************************************

import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yposistion = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.penup()
    new_turtles.goto(x=-230, y=yposistion[turtle_index])
    new_turtles.color(colors[turtle_index])
    all_turtles.append(new_turtles)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have win! The {winning_color} turtle win")
            else:
                print(f"You lose! The {winning_color} turtle win")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()