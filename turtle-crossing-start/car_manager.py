from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.generate_cars()



    def generate_cars(self):

        car = Turtle("square")
        car.penup()
        car.setposition(280, random.randint(-300, 300))
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        self.cars.append(car)

    def move_cars(self):

        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)



