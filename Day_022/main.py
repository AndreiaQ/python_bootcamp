from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
paddle = Turtle()


def move_up():
    y = paddle.ycor()
    paddle.sety(y + 20)


def move_down():
    y = paddle.ycor()
    paddle.sety(y - 20)

paddle.color("white")
paddle.shape("square")
paddle.shapesize(5,1,1)
paddle.penup()
paddle.goto(350,0)
screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")






screen.exitonclick()




