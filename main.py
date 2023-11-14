from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong - The classic arcade game!")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # Needs to go back other way
        ball.bounce_x()

    # Detect when ball misses right paddle
    if ball.xcor() > 380:
        ball.miss()
        ball.move()
        scoreboard.clear()
        scoreboard.l_point()

    # Detect when ball misses left paddle
    if ball.xcor() < -380:
        ball.miss()
        ball.move()
        scoreboard.clear()
        scoreboard.r_point()

screen.exitonclick()
