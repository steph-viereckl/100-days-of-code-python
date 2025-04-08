from turtle import Turtle
from brick import Brick
from draw import Draw

rows = [
    {
        "color": "red",
        "y_cor": 450
    },
    {
        "color": "red",
        "y_cor": 400
    },
    {
        "color": "yellow",
        "y_cor": 350
    },
    {
        "color": "yellow",
        "y_cor": 300
    },
    {
        "color": "green",
        "y_cor": 250
    },
    {
        "color": "green",
        "y_cor": 200
    }
]


class Builder(Turtle):

    def __init__(self):
        super().__init__()

        self.bricks = []

        for row in rows:

            starting_x_cor = -700
            # while starting_x_cor <= -700:
            while starting_x_cor <= 700:
                new_brick = Brick(row["color"], starting_x_cor, row["y_cor"])
                starting_x_cor += 175
                self.bricks.append(new_brick)

                # For -700, 200...
                # The width of the square will be between -780 and -620
                # The height of the square will be between 220 and 200
                # x_lower_range = new_brick.xcor() - 80
                # x_higher_range = new_brick.xcor() + 80
                # y_lower_range = new_brick.ycor() - 20
                # y_higher_range = new_brick.ycor() + 20

                # print(f"x_lower_range: {x_lower_range}, x_higher_range: {x_higher_range}, y_lower_range: {y_lower_range}, y_higher_range: {y_higher_range},")
                # Draw dummy lines to visualize the edges of the box
                # draw = Draw(x_lower_range, x_higher_range, y_lower_range, y_higher_range)

