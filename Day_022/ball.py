from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0,0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed(1)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def rebounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_out_of_bounds(self):
        if abs(self.xcor()) > 380:
            self.setposition(0, 0)
            self.move_speed = 0.1
            self.rebounce()


