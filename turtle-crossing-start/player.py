from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('DarkTurquoise')
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.start_level = 0

    def movement(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def cross_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


