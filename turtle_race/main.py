import random
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color:\n 'red',"
                                                          " 'orange', 'yellow', 'green', 'blue', 'purple'")
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-90, -50, -10, 30, 70, 110]
all_turtle = []
is_race_on = False


for index in range(6):
    turtle = Turtle(shape='turtle')
    turtle.color(color[index])
    turtle.penup()
    turtle.goto(x=-230, y=y_position[index])
    all_turtle.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've win! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
