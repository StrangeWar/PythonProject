import turtle
from turtle import Turtle, Screen
import random

color_list = [(5, 25, 68), (42, 8, 23), (40, 84, 132), (24, 10, 5), (14, 60, 128), (5, 13, 8), (138, 63, 106),
              (136, 22, 74), (126, 83, 57), (205, 73, 134), (206, 125, 166), (81, 97, 91), (120, 36, 27),
              (196, 147, 102), (105, 90, 202), (92, 71, 20), (175, 144, 52), (138, 144, 172), (249, 152, 189),
              (193, 94, 79), (250, 218, 199), (252, 194, 215), (135, 153, 147), (44, 77, 67), (41, 73, 79),
              (236, 207, 89), (108, 135, 141), (101, 145, 135), (238, 171, 160), (52, 33, 226), (255, 3, 67),
              (174, 160, 235), (240, 205, 0), (133, 221, 197), ]


def random_color():
    colour = random.choice(color_list)
    return colour


turtle.colormode(255)
shiro = Turtle()
shiro.hideturtle()
shiro.penup()
shiro.speed("fastest")
screen = Screen()
shiro.shape('arrow')
gap = 0
shiro.setposition(-225, -225)

for _ in range(10):
    gap += 50
    for i in range(10):
        shiro.dot(20, random_color())
        shiro.forward(50)
    shiro.setx(-225)
    shiro.sety(-225 + gap)

screen.exitonclick()
