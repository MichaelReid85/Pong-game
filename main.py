import turtle
from turtle import Turtle, Screen

paddle = Turtle()

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong - The classic arcade game!")

paddle.penup()
paddle.color("black")
paddle.speed("fastest")
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.setposition(350, 0)
paddle.color("white")


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() +-20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")





screen.exitonclick()