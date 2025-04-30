from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,3,1)
        color = random.choice(COLORS)
        self.color(color)
        self.penup()
        y = random.randint(-250,250)
        self.setposition(350, y)

    def move_car(self, car_speed):
        x = self.xcor()
        self.setx(x - car_speed)







