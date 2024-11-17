from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, starting_x_coordinate):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.segments = []
        self.setheading(0)
        self.speed("fastest")

        starting_y_coordinates = [-30, -10, 10, 30, 50]
        starting_coordinates = []

        for position in starting_y_coordinates:
            starting_coordinates.append((starting_x_coordinate, position))

        # self.head = self.segments[0]
        for position in starting_coordinates:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle()
        new_square.penup()
        new_square.shape("square")
        new_square.color("white")
        new_square.setposition(position)
        self.segments.append(new_square)

    #       90
    # 180 <    > 0
    #       270

    def up(self):

        for segment in self.segments:
            segment.setheading(90)
            segment.forward(20)

    def down(self):

        for segment in self.segments:
            segment.setheading(270)
            segment.forward(20)

    def check_hit(self, ball_ycor):

        print(f'check hit ball ycor: {ball_ycor}')
        print(f'self.segments[0].ycor(): {self.segments[0].ycor()}')
        print(f'self.segments[-1].ycor(): {self.segments[-1].ycor()}')

        #  If the ball is between the paddle's top segment and the bottom segment
        if ball_ycor >= self.segments[0].ycor() and ball_ycor <= self.segments[-1].ycor():
            print("hit the right paddle! Change direction")
            return True
        else:
            print("you lose!")
            return False