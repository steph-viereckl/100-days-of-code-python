from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")
SCORE = "Score: "
HIGH_SCORE = "High Score: "
GAME_OVER = "GAME OVER"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.setposition(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(align=ALIGNMENT, move=False, arg=f"{SCORE}{self.score} {HIGH_SCORE}{self.high_score}",
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write(arg=GAME_OVER, font=FONT, align=ALIGNMENT)

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0