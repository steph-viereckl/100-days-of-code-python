from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
PROBABILITY_OF_CAR = 20


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []

        # For every 10th y coordinate, create car
        for x_cor in range(-300, 300, 10):
            self.generate_car(x_cor)



    def generate_car(self, x_cor):

        # Only generate a car a fraction of the time
        if random.randint(0, 100) <= PROBABILITY_OF_CAR:
            car = Turtle("square")
            car.penup()
            car.setposition(x_cor, random.randint(-300, 300))
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def move_cars(self):

        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)



