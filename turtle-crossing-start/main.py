import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.move_up, key="Up")
screen.onkey(turtle.move_down, key="Down")


# 1. Create Turtle and move it up across the screen
# 2. When it reaches the top of the screen, it levels up
# 3. Add randomly generated cars
# 4. Detect collision with car and display game over
# 5. When it reaches the top of the screen, increase speed of cars


game_is_on = True
while game_is_on:

    time.sleep(.1)
    screen.update()

    if turtle.ycor() > 300:
        scoreboard.level += 1
        scoreboard.update_score()
        turtle.reset()

    car_manager.generate_car(300)
    car_manager.move_cars()

    for car in car_manager.cars:

        # TODO I think that this can be improved so it is more specific
        if car.distance(turtle) < 20:

            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()