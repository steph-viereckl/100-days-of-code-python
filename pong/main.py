from turtle import Screen
from scoreboard import Gameboard, Score
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 1500
X_COR_WIDTH = int(SCREEN_WIDTH / 2)
SCREEN_HEIGHT = 1000
Y_COR_HEIGHT = int(SCREEN_HEIGHT / 2)
RIGHT_PADDLE_X_COR = 700
LEFT_PADDLE_X_COR = -700

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
    time.sleep(0.05)
    ball.move()

    # Hit the ceiling
    print(f"ball ycor is {ball.ycor()} and top of screen is {Y_COR_HEIGHT - 20}")
    if ball.ycor() == (Y_COR_HEIGHT - 20):
        ball.go_up = False

    # Hit the floor
    if ball.ycor() == -1 * Y_COR_HEIGHT + 20:
        ball.go_up = True

    if ball.xcor() == RIGHT_PADDLE_X_COR - 20:

        hit_paddle = right_paddle.check_hit(ball_ycor = ball.ycor())

        if hit_paddle is True:
            ball.go_right = False  # Change ball direction to go left
        else:
            game_is_on = False
            gameboard.game_over()

    elif ball.xcor() == LEFT_PADDLE_X_COR + 20:

        hit_paddle = left_paddle.check_hit(ball_ycor=ball.ycor())

        if hit_paddle is True:
            ball.go_right = True  # Change ball direction to go right
        else:
            game_is_on = False
            gameboard.game_over()


    # TODO Now that the score is displayed need to update score

    # End of While Loop

screen.exitonclick()
