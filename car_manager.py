from turtle import Turtle, Screen
import random

import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
BOTTEM_LIMIT = -250
TOP_LIMIT = 250
# ycor = random.randint(BOTTEM_LIMIT, TOP_LIMIT)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(280, random.randint(BOTTEM_LIMIT, TOP_LIMIT))
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10