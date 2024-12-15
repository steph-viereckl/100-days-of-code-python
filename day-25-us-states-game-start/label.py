from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roman", 10, "normal")


class StateLabel(Turtle):

    def __init__(self, state_df):
        super().__init__()

        state_name = state_df.state.item()
        x_cor = state_df.x.item()
        y_cor = state_df.y.item()

        self.hideturtle()
        self.penup()
        self.setposition(x_cor, y_cor)
        self.write(align=ALIGNMENT, move=False, arg=state_name, font=FONT)