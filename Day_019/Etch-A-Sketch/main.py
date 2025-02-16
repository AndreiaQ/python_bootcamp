from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_counter_clockwise():
    t.left(10)

def move_clockwise():
    t.right(10)

def clear_drawing():
    t.penup()
    t.clear()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_drawing, "c")
screen.exitonclick()