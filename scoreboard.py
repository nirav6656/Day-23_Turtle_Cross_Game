from turtle import Turtle,Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-230,230)
        self.score = 0
        self.write(self.score, align="left", font=FONT)


    def update_score(self):
        self.clear()
        self.score +=1
        self.write(self.score, align="left", font=FONT)

