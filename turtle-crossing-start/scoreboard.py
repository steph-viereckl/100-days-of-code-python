from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEFT_ALIGN = "Left"
CENTER_ALIGN = "Center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        sel
        self.penup()
        self.hideturtle()
        self.setposition(-260, 260)
        self.write(arg=f"Level: {self.level}", font=FONT, align=LEFT_ALIGN, move=False)

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align=LEFT_ALIGN, move=False)

    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.write(arg=f"Game Over", font=FONT, align=CENTER_ALIGN, move=False)

