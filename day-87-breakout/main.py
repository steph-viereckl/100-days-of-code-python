# TODO Create Bricks
# TODO Make Ball Hit Brick and Break Brick.
# TODO When bigger bricks are hit, speed increases
# TODO Create Scoreboard and increase score
# TODO When user loses, they have 3 lives and then game over

#--------------- Imports -----------------#
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
import time

#--------------- Constants -----------------#

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
X_COR_WIDTH = int(SCREEN_WIDTH / 2)
Y_COR_HEIGHT = int(SCREEN_HEIGHT / 2)
SLEEP_TIMER = 0.1

#--------------- UI -----------------#

# Setup screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Stephanie's Breakout Game")
screen.bgcolor("black")
screen.tracer(0) # Turn off tracer
screen.listen()

# Setup Ball
ball = Ball()
# Setup Paddle
paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT)

game_is_on = True

while game_is_on:

    # Update screen every .1 second
    screen.update()
    time.sleep(SLEEP_TIMER)

    # Move ball
    ball.move()

    # Detect hitting ceiling
    if ball.ycor() >= (Y_COR_HEIGHT - ball.buffer):
        ball.go_up = False

    # Detect hitting right wall
    if ball.xcor() >= (X_COR_WIDTH - ball.buffer):
        ball.go_right = False

    # Detect hitting left wall
    if ball.xcor() <= -(X_COR_WIDTH - ball.buffer):
        ball.go_right = True

    if ball.ycor() <= -440:

        print(f"Ball is at {ball.xcor()}")

        left_paddle_edge = paddle.xcor() - 150
        right_paddle_edge = paddle.xcor() + 150
        print(f"Paddle between {left_paddle_edge} and {right_paddle_edge}")

        if left_paddle_edge < ball.xcor() < right_paddle_edge:
            print("Between!")
            ball.go_up = True
            ball.go_right = not ball.go_right

    # Move paddle based on user's mouse
    paddle.move(paddle.screen.cv.winfo_pointerx())




screen.exitonclick()
