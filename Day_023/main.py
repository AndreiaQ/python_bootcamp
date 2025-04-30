import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

cars = []
car_speed = 5

screen.onkey(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1,8) == 1:
        new_car= CarManager()
        cars.append(new_car)

    for car in cars:
        car.move_car(car_speed)

    if player.ycor() > 280:
        player.setposition(0, -280)
        scoreboard.increase_score()
        car_speed += 10

    for car in cars:
        if abs(player.xcor() - car.xcor()) < 25 and abs(player.ycor() - car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False
            break
screen.update()









