from turtle import Turtle

STARTING_COORDINATES = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    # Constructor
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_COORDINATES:
            self.add_segment(position)


    def add_segment(self, position):
        new_square = Turtle()
        new_square.penup()
        new_square.shape("square")
        new_square.color("white")
        new_square.setposition(position)
        self.segments.append(new_square)

    def extend(self):
        # Get the last segment by the last index's position
        self.add_segment(self.segments[-1].position())

    def move(self):

        # Get number of segments in snake
        snake_length = (len(self.segments))

        # Range Parameters are (Start, Stop, Step)
        # Set start to be the last index (length - 1)
        # Set stop to be 0 (first segment in list)
        # Decrease step by -1
        for i in range((snake_length - 1), 0, -1):

            # Get segment before the current segment
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()

            # Tell current segment to go to space of the segment before it
            self.segments[i].goto(new_x, new_y)

        # Move the first segment forward
        self.head.forward(MOVE_DISTANCE)


    #       90
    # 270 <    > 0
    #      180

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):

        for segment in self.segments:
            segment.goto(1000,1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]




