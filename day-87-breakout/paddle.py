from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.screen_width = width
        self.y_cor = -((height / 2) - 50)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=15)
        self.setheading(0)
        self.speed("fastest")
        self.setposition(0, self.y_cor)
        self.showturtle()

    def move(self, x):

        #TODO Consider making these values more dynamic if screen width changes
        # To get cursor in the middle of the paddle
        new_x = x - 865

        # If mouse is off screen to the left, put paddle furthest left
        if new_x < -580:
            self.goto(-580, self.y_cor)

        # If mouse is off screen to the right, put paddle furthest right
        elif new_x > 580:
            self.goto(580, self.y_cor)

        # Otherwise, put paddle to user's cursor
        else:
            self.goto(new_x, self.y_cor)
