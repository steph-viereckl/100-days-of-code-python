from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 30, "normal")
GAME_OVER = "GAME OVER"

SOUTH = 270

class Gameboard(Turtle):
    """Dotted Lines Down the center of the board"""
    def __init__(self, screen_height):
        super().__init__()
        self.penup()
        self.shapesize(.5)
        self.top_of_screen = screen_height/2
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

class Scoreboard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, (screen_height/2)*.9)
        self.write(align=ALIGNMENT, move=False, arg=f"TEST TITLE", font=FONT)


