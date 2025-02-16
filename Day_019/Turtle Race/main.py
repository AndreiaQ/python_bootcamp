from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green" , "blue", "purple"]

y_positions = [-100, -70, -40, -10, 20, 50]

turtles = []

for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-220, y_positions[i])
    turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won the bet!")
            else:
                print(f"You lost the bet! The winning color is {winning_color}!")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()