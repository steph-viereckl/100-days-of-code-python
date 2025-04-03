from turtle import Turtle
import random


LOW = 10
MEDIUM = 20
HIGH = 30

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setposition(0, -400)
        self.setheading(90)
        self.showturtle()
        self.speed = 10
        self.buffer = 20

        # Always start with ball moving up
        self.go_up = True
        # Randomly start ball going right or left
        self.go_right = random.choice([True, False])

        # Test ball immediately coming at paddle
        self.go_up = False
        self.setposition(0, -200)

    def move(self):

        # Adjust left or right by 10
        if self.go_right is True:
            new_x = self.xcor() + self.speed
        else:  # Otherwise we know it is going "left"
            new_x = self.xcor() - self.speed

        # Adjust up or down by 10
        if self.go_up is True:
            new_y = self.ycor() + self.speed
        else:  # Otherwise we know it is going "down"
            new_y = self.ycor() - self.speed

        self.goto(new_x, new_y)

