from turtle import Turtle, Screen, colormode
import random

colormode(255)

turtle = Turtle
turtle.width(8)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

turtle.forward(100)

screen = Screen()
screen.exitonclick()
