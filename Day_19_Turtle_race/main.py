import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = ""
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet",
                                prompt="Which turtle will win the race? Enter a color:\n(red, orange, yellow, green, "
                                "blue, purple)").lower()
y_coord = [125, 75, 25, -25, -75, -125]
y_coord_line = [150, 100, 50, 0, -50, -100, -150]
all_turtles = []

for race_lines in range(0,7):
    race_line = Turtle()
    race_line.hideturtle()
    race_line.speed("fastest")
    race_line.penup()
    race_line.goto(x=-250, y=y_coord_line[race_lines])
    race_line.pendown()
    race_line.forward(500)

finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.speed("fastest")
finish_line.goto(x=225, y=250)
finish_line.setheading(270)
finish_line.pendown()
finish_line.forward(500)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_coord[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
