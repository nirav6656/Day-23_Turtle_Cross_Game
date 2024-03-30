from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.width(2)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def up(self):
        self.forward(MOVE_DISTANCE)


    def gamover(self):
        self.write("Game Over", align="center")



