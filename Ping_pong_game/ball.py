from turtle import Turtle

BALL_SPEED = .1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.y_move = 10
        self.x_move = 10
        self.ball_speed = BALL_SPEED

    def move(self):
        """Provides movement to ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        """Enable the ball to bounce back on hitting the top and the bottom wall."""
        self.y_move *= -1

    def x_bounce(self):
        """Enable the to bounce back on hitting the paddles."""
        self.x_move *= -1
        # Increases the speed of ball on every hit by paddles.
        self.ball_speed *= 0.9

    def reset_position(self):
        """Resets the position and speed of ball when missed by any paddle."""
        self.goto(0, 0)
        self.ball_speed = BALL_SPEED
        self.x_bounce()

