from turtle import Screen
from unittest.mock import right

from scoreboard import Gameboard, Scoreboard
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
RIGHT_PADDLE_X_COR = 700
LEFT_PADDLE_X_COR = -700

# Setup screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Steph's Pong Game")
screen.tracer(0) # Turn off tracer

gameboard = Gameboard(SCREEN_HEIGHT) # Setup Striped Line
scoreboard = Scoreboard(SCREEN_HEIGHT)
right_paddle = Paddle(starting_x_coordinate=RIGHT_PADDLE_X_COR)
left_paddle = Paddle(starting_x_coordinate=LEFT_PADDLE_X_COR)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, key="Up")
screen.onkey(right_paddle.down, key="Down")
screen.onkey(left_paddle.up, key="e")
screen.onkey(left_paddle.down, key="f")

game_is_on = True

while game_is_on:

    # Update screen every .1 second
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Hit the ceiling
    if ball.ycor() == ((SCREEN_HEIGHT/2) - 20):
        ball.go_up = False

    # Hit the floor
    if ball.ycor() == -((SCREEN_HEIGHT/2) - 20):
        ball.go_up = True

    if ball.xcor() == RIGHT_PADDLE_X_COR - 20:

        #  If the ball is between the right paddle's top segment and the bottom segment
        if ball.ycor() >= right_paddle.segments[0].ycor() and ball.ycor() <= right_paddle.segments[-1].ycor():
            print("hit the right paddle! Change direction")
            ball.go_right = False  # Turn Left
        else:
            print("you lose!")
            game_is_on = False

    if ball.xcor() == LEFT_PADDLE_X_COR + 20:

        #  If the ball is between the left paddle's top segment and the bottom segment
        if ball.ycor() >= right_paddle.segments[0].ycor() and ball.ycor() <= right_paddle.segments[-1].ycor():
            print("hit the right paddle! Change direction")
            ball.go_right = False  # Turn Left
        else:
            print("you lose!")
            game_is_on = False

# For tomorrow, trying to figure out the best way to organize this so it is less code in the main class
# Should i put this in the paddle or the ball class maybe?



screen.exitonclick()
