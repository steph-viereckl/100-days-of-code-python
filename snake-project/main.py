# TODO #1 Create Snake Body
# Create 3 squares on the screen
# Each square will be its own turtle
# Turtles are 20 x 20 pixels

# TODO #2 Move the squares
# Tell it to change directions

# TODO #3 Control the Snake
# Use keyboard controals (up down left right arrows)

# TODO #4 Put & Detect Food
# After eating food create new food and increase length

# TODO #5 Create Scoreboard

# TODO #6 Detect collision with Wall

# TODO #7 Detect collision with Snake

#############################################

from turtle import Screen
import time
from snake import Snake

# Setup screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Steph's Snake Game")
screen.tracer(0) # Turn off tracer

# Create Snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:

    # Update screen every .1 second
    screen.update()
    time.sleep(0.1)

    snake.move()





screen.exitonclick()
