import colorgram
import turtle
import random

t = turtle.Turtle()
colors = colorgram.extract("image.png", 25)
turtle.colormode(255)

t.speed("fastest")
color_list = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181)]

def drawing_circles(random_color):
    t.fillcolor(random_color)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.forward(50)


t.penup()
x_start, y_start = -250, -200
t.goto(x_start, y_start)

for i in range(10):

    for j in range(10):
        random_color_chosen = random.choice(color_list)
        drawing_circles(random_color_chosen)

    y_start +=50
    t.goto(x_start, y_start)


screen = turtle.Screen()
screen.exitonclick()
