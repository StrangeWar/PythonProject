import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score_board import Score


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Ping-Pong-Game")
screen.tracer(0)

r_paddle = Paddle(x_position=370, y_position=0)
l_paddle = Paddle(x_position=-370, y_position=0)
ball = Ball()
score = Score()

# Control of the paddles
screen.listen()
screen.onkeypress(fun=r_paddle.up, key='Up')
screen.onkeypress(fun=r_paddle.down, key='Down')
screen.onkeypress(fun=l_paddle.up, key='w')
screen.onkeypress(fun=l_paddle.down, key='s')

while score.game_on:

    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision of ball with top and bottom walls and bounces the ball.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision of ball with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.x_bounce()

    # Ball missed by Right paddle.
    if ball.xcor() > 400:
        ball.reset_position()
        score.l_point()

    # Ball missed by Left paddle.
    if ball.xcor() < -400:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
