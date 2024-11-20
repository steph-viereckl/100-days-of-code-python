from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.showturtle()

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.forward(-10)

    def reset(self):
        self.goto(STARTING_POSITION)
