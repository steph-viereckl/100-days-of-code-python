from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")
TITLE = "Score: "
GAME_OVER = "GAME OVER"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(align=ALIGNMENT, move=False, arg=f"{TITLE}{self.score}",
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.home()
        self.write(arg=GAME_OVER, font=FONT, align=ALIGNMENT)

