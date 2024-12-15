from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roman", 10, "normal")


class StateLabel(Turtle):

    def __init__(self, state_df):
        super().__init__()
        # Get x cor from series and y cor

        self.hideturtle()
        self.penup()
        self.color("black")

        print(f"state.state: {state_df.state.item()}")

        state_name = state_df.state.item()
        x_cor = state_df.x.item()
        y_cor = state_df.y.item()

        print(f"state.x: {x_cor}")
        print(f"state.y: {y_cor}")
        print(f"state.state: {state_name}")

        self.setposition(x_cor, y_cor)
        self.write(align=ALIGNMENT, move=False, arg=state_name, font=FONT)