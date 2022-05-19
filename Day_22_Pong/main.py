from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # if ball.xcor() > 320 and (r_paddle.ycor() + 50) < ball.ycor() > (r_paddle.ycor() - 50):
    #     ball.bounce_x()
    # print(f"paddle_y: {r_paddle.ycor()}")
    # print(f"ball_y: {int(ball.ycor())}")
    # print(f"ball_x: {int(ball.xcor())}")

    # R_paddle misses
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # L_paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
