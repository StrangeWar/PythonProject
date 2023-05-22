import random
import time
from turtle import Screen


from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
player = Player()
car_manger = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.movement, key='Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manger.create_car()
    car_manger.move_car()

    # Detect collision of turtle with car.
    for car in car_manger.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect player cross the finish line.
    if player.cross_finish_line():
        player.go_to_start()
        car_manger.speedup()
        scoreboard.level_up()
screen.exitonclick()

