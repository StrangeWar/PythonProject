from turtle import Turtle, Screen

shiro = Turtle()
screen = Screen()


def forward():
    shiro.forward(10)


def backward():
    shiro.back(10)


def anticlockwise():
    shiro.left(10)


def clockwise():
    shiro.right(10)


def screen_clear():
    screen.reset()

screen.listen()

screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key='s', fun=backward)
screen.onkeypress(key='a', fun=anticlockwise)
screen.onkeypress(key='d', fun=clockwise)
screen.onkeypress(key='c', fun=screen_clear)
screen.exitonclick()