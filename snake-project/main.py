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

from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Setup screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Steph's Snake Game")
screen.tracer(0) # Turn off tracer

# Create Snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food using distance() method
    # If distance is less than 15 pixels, we think it collides
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail - Slice from index 1 to end of list
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
