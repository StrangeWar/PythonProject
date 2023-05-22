from turtle import Turtle

# Movement speed of paddles.
SPEED = 100


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.resizemode('user')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_position, y=y_position)

    def up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)
