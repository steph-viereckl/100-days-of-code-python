from turtle import Turtle

class Brick(Turtle):

    def __init__(self, color, x_cor, y_cor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=8)
        self.setposition(x=x_cor, y=y_cor)

        # Print out the position to help with troubleshooting
        # style = ('Courier', 12, 'italic')
        # message = f"x: {self.xcor()} y: {self.ycor()}"
        # self.write(message, font=style, align='center')
        self.showturtle()