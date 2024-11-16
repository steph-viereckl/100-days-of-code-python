from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("yellow")
        # Start out moving ball up and to the right
        self.go_up = random.choice([True, False])
        self.go_right = random.choice([True, False])

    def move(self):

        # Adjust left or right by 10
        if self.go_right is True:
            new_x = self.xcor() + 10
        else: #  Otherwise we know it is going "left"
            new_x = self.xcor() - 10

        # Adjust up or down by 10
        if self.go_up is True:
            new_y = self.ycor() + 10
        else: #  Otherwise we know it is going "down"
            new_y = self.ycor() - 10

        self.goto(new_x, new_y)


