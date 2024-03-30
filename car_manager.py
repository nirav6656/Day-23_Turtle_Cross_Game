from turtle import Turtle, Screen
import random

import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
BOTTEM_LIMIT = -250
TOP_LIMIT = 250
ycor = random.randint(BOTTEM_LIMIT, TOP_LIMIT)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.generate_car()

    def generate_car(self):
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(280, ycor)
        self.color(random.choice(COLORS))
        self.shape("square")
        self.setheading(180)
        self.count = 0
        for _ in range(600):
            time.sleep(0.01)
            Screen().update()
            self.forward(1)
            self.count += 1
            if self.count >= 6:
                self.generate_car()
                self.count = 0
