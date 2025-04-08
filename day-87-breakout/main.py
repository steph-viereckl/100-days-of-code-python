
#--------------- Imports -----------------#
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from builder import Builder
import time

#--------------- Constants -----------------#

SCREEN_WIDTH = 1605
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
# Create wall of bricks
wall = Builder()

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

    y_buffer = 33
    x_buffer = 88

    # TODO Increase speed of ball when a new "row" is hit
    for brick in wall.bricks:

        x_lower_range = brick.xcor() - x_buffer
        x_higher_range = brick.xcor() + x_buffer
        y_lower_range = brick.ycor() - y_buffer
        y_higher_range = brick.ycor() + y_buffer

        # TODO need to improve so if we hit the side of a brick it bounces
        if (x_lower_range <= ball.xcor() <= x_higher_range) and (y_lower_range <= ball.ycor() <= y_higher_range):
            ball.bounce()
            brick.hideturtle()
            wall.bricks.remove(brick)
            break

    # Ball is at paddle/ground level
    if ball.ycor() <= -440:

        # Get the edges of the paddle
        left_paddle_edge = paddle.xcor() - 175
        right_paddle_edge = paddle.xcor() + 175
        print(f"Paddle between {left_paddle_edge} and {right_paddle_edge}")

        # Hit the paddle!
        if left_paddle_edge < ball.xcor() < right_paddle_edge:

            ball.go_up = True

            # If the ball hit the left side of the paddle, bounce to the left
            if ball.xcor() < paddle.xcor():
                ball.go_right = False
            # If the ball hit the right side of the paddle, bounce to the right
            else:
                ball.go_right = True

        # Miss the paddle
        else:
            print("You lose!")
            # TODO if ball hits floor lose a point
            ball.bounce() # Just bounce right now so we can keep playing
            # game_is_on = False

    # Move paddle based on user's mouse
    paddle.move(paddle.screen.cv.winfo_pointerx())

screen.exitonclick()
