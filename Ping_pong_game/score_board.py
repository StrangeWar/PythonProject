from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.game_on = True

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('courier', 60, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('courier', 60, 'normal'))

    def l_point(self):
        """Increases the score of left player by one when right player misses the ball."""
        self.l_score += 1
        self.update_score()

        # if left player hits 10 points its game over and left player wins the game.
        if self.l_score == 5:
            self.goto(0, 0)
            self.write("GAME OVER! Left player Wins.", align='center', font=('courier', 20, 'normal'))
            self.game_on = False

    def r_point(self):
        """Increases the score of right player by one when left player misses the ball."""
        self.r_score += 1
        self.update_score()

        # if right player hits 10 points its game over and right player wins the game.
        if self.r_score == 5:
            self.goto(0, 0)
            self.write("GAME OVER! right player Wins.", align='center', font=('courier', 20, 'normal'))
            self.game_on = False
