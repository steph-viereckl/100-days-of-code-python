from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Verdana", 100, "normal")
GAME_OVER_FONT = ("Verdana", 100, "normal")
GAME_OVER = "GAME OVER"

SOUTH = 270

class Gameboard(Turtle):
    """Dotted Lines Down the center of the board"""
    def __init__(self, y_cor_height):
        super().__init__()
        self.penup()
        self.shapesize(.5)
        self.top_of_screen = y_cor_height
        self.bottom_of_screen = -1 * self.top_of_screen
        self.goto(0, self.top_of_screen)
        self.shape("square")
        self.color("white")
        self.speed("slowest")
        self.setheading(SOUTH)

        # Draw dotted line from top to bottom of screen
        while self.ycor() > self.bottom_of_screen:

            # TODO make the steps forward be more dynamic
            for num in range(3):
                self.stamp()
                self.forward(10)

            self.forward(30)

    def game_over(self):
        self.home()
        self.write(arg=GAME_OVER, font=GAME_OVER_FONT, align=ALIGNMENT)

class Score(Turtle):

    def __init__(self, x_cor_width, y_cor_height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(x_cor_width * .2, y_cor_height * .7)
        self.write(align=ALIGNMENT, move=False, arg=f"1", font=SCORE_FONT)

# class Scoreboard(Turtle):
#
#     def __init__(self, y_cor_height):
#         super().__init__()
#         self.hideturtle()
#         self.penup()
#         self.color("white")
#         self.setposition(0, y_cor_height * .9)
#         self.write(align=ALIGNMENT, move=False, arg=f"TEST TITLE", font=FONT)


