import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")
carmanager = CarManager()
score = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.generate_car()
    carmanager.move_car()
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            player.gamover()
    if player.ycor()>300:
        player = Player()
        carmanager.increase_speed()
        scoreboard.update_score()
        screen.onkey(player.up, "Up")



screen.exitonclick()