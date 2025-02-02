from turtle import Turtle, Screen, colormode
import random

colormode(255)

turtle = Turtle()
turtle.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_polygon(sides, side_length=100):
    turtle.color(random_color())
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(side_length)
        turtle.right(angle)

for sides in range(3, 11):
    draw_polygon(sides)

screen = Screen()
screen.exitonclick()
