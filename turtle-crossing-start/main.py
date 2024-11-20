import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# 1. Create Turtle and move it up across the screen
# 2. When it reaches the top of the screen, it levels up
# 3. Add randomly generated cars
# 4. Detect collision with car and display game over
# 5. When it reaches the top of the screen, increase speed of cars

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()



screen.exitonclick()