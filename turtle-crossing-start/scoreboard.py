from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(-285, 265)
        self.update_score()

    def update_score(self):
        self.write(f"Level:{self.level}", align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align='center', font=FONT)
