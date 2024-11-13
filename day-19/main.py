# Higher Order Functions - functions that can work within another
# TIP! When you have a function you didn't create yourself, use keyword arguments
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_y_position = [-125, - 75, -25, 25, 75, 125]
user_bet = screen.textinput(title="Make your bet!", prompt="Which color turtle will in?")

race_is_going = True
racers = []

for i in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = starting_y_position[i])
    racers.append(new_turtle)

while race_is_going:

    for turtle in racers:

        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race_is_going = False

            if winner == user_bet:
                print("You've won!")
            else:
                print(f"{winner} turtle has won! You lose!")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)





# Start Screen Listener
screen.listen()





screen.exitonclick()