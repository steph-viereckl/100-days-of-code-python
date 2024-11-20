from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "Left"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setposition(-260, 260)
        self.write(arg=f"Level: {self.level}", font=FONT, align=ALIGNMENT, move=False)

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align=ALIGNMENT, move=False)

