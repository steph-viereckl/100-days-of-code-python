from turtle import Turtle

# This is just a dummy class to help figure out where the edges of the bricks are
class Draw(Turtle):

    def __init__(self, low_x, high_x, low_y, high_y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("pink")
        self.setposition(high_x, high_y)
        self.pendown()
        self.color("blue")
        self.goto(high_x, low_y)
        self.color("green")
        self.goto(low_x, low_y)
        self.color("yellow")
        self.goto(low_x, high_y)
        self.color("red")
        self.goto(high_x, high_y)
