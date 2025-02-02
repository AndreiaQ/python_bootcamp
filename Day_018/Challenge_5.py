from turtle import Turtle, Screen, colormode
import random

colormode(255)

turtle = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

angle = 0
turtle.speed(0)

for i in range(100):
    turtle.color(random_color())
    turtle.circle(100)
    angle += 3.6
    turtle.setheading(angle)


screen = Screen()
screen.exitonclick()
