import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
shiro = Turtle()
screen = Screen()
screen.bgcolor('black')
shiro.shape('arrow')
shiro.pensize(10)
shiro.speed(7)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def angles():
    random_angles = random.choice([90, 270, 180, 0])
    return random_angles


def random_walk(angel, color):
    shiro.color(color)
    shiro.forward(20)
    shiro.setheading(angel)


for _ in range(200):
    random_walk(angles(), random_colors())

screen.exitonclick()
