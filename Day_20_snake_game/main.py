from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.right, key="d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
