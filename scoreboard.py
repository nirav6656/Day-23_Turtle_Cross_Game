from turtle import Turtle,Screen
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.score = 0
        self.write(f"Your Score is {self.score}", align="left", font=FONT)


    def update_score(self):
        self.clear()
        self.score +=1
        self.write(f"Your Score is {self.score}", align="left", font=FONT)

    def gamover(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("courier", 80, "normal" ))