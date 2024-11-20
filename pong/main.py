from turtle import Screen
from scoreboard import Gameboard, Score
from paddle import Paddle
from ball import Ball
import time

# TODO Do some visual clean ups? Change font?

SCREEN_WIDTH = 1500
X_COR_WIDTH = int(SCREEN_WIDTH / 2)
SCREEN_HEIGHT = 1000
Y_COR_HEIGHT = int(SCREEN_HEIGHT / 2)
RIGHT_PADDLE_X_COR = 700
LEFT_PADDLE_X_COR = -700
SLEEP_TIMER = 0.05

# Setup screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Stephanie's Pong Game")
screen.tracer(0) # Turn off tracer

gameboard = Gameboard(Y_COR_HEIGHT) # Setup Striped Line

left_player_score = Score(-X_COR_WIDTH, Y_COR_HEIGHT)
right_player_score = Score(X_COR_WIDTH, Y_COR_HEIGHT)
ball = Ball(Y_COR_HEIGHT)
right_paddle = Paddle(starting_x_coordinate=RIGHT_PADDLE_X_COR)
left_paddle = Paddle(starting_x_coordinate=LEFT_PADDLE_X_COR)

screen.listen()
screen.onkey(right_paddle.up, key="Up")
screen.onkey(right_paddle.down, key="Down")
screen.onkey(left_paddle.up, key="e")
screen.onkey(left_paddle.down, key="f")

game_is_on = True

while game_is_on:

    # Update screen every .1 second
    screen.update()
    time.sleep(SLEEP_TIMER)
    ball.move()

    # Hit the ceiling
    if ball.ycor() == (Y_COR_HEIGHT - 20):
        ball.go_up = False

    # Hit the floor
    if ball.ycor() == -1 * Y_COR_HEIGHT + 20:
        ball.go_up = True

    if ball.xcor() == RIGHT_PADDLE_X_COR - 20:

        if ball.distance(right_paddle) < 60:
            ball.go_right = False  # Change ball direction to go left
        else:
            # Keep ball moving even though we know it hit the wall
            for num in range(5):
                screen.update()
                time.sleep(SLEEP_TIMER)
                ball.move()

            left_player_score.increase_score()
            ball.reset()

    elif ball.xcor() == LEFT_PADDLE_X_COR + 20:

        if ball.distance(left_paddle) < 60:
            ball.go_right = True  # Change ball direction to go left

        else:
            # Keep ball moving even though we know it hit the wall
            for num in range(5):
                screen.update()
                time.sleep(SLEEP_TIMER)
                ball.move()

            right_player_score.increase_score()
            ball.reset()

    # End of While Loop

screen.exitonclick()
