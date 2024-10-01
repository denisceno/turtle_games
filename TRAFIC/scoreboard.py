from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-250, 250)
        self.new_score()

    def new_score(self):
        self.clear()
        self.write(f"Level :{self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def new_level(self):
        self.level += 1
        self.new_score()
