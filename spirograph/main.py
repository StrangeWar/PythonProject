import turtle
from turtle import Turtle, Screen
import random

circle = Turtle()
turtle.colormode(255)
screen = Screen()
screen.bgcolor('black')
circle.shape('arrow')
circle.speed('fastest')


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def spirograph(size):
    for _ in range(int(360/size)):
        circle.color(random_colors())
        circle.circle(100)
        current_pos = circle.heading()
        circle.setheading(current_pos + size)


spirograph(10)


screen.exitonclick()