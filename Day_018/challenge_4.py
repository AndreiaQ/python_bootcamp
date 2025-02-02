from turtle import Turtle, Screen, colormode
import random

colormode(255)

turtle = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def random_walk():
    random_number = random.randint(1,4)
    if random_number == 1:
        turtle.forward(100)
    elif random_number == 2:
        turtle.back(100)
    elif random_number == 3:
        turtle.right(100)
    elif random_number == 4:
        turtle.left(100)


turtle.width(9)
turtle.speed(0)

for i in range(100):
    turtle.color(random_color())
    random_walk()
    i += 1

screen = Screen()
screen.exitonclick()
