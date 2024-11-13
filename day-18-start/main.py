# If you are only going to use something once or twice, just import the whole module
#import turtle
# tim = turtle.Turtle()

# Otherwise, import specific classes
# This makes it easier to access the classes without writing the module
from turtle import Turtle, Screen

# You can also give it as an alias
# import turtle as t
# tim = t.Turtle()

# Can also just use the wildcard. But it is hard to trace origins with this
# from turtle import *

# Turtle is included in the base library
# To import other packages, we go to PyPi (Python Packages)

# PyCharm is smart and will suggest you to install is (hover to install)
# .venv is the "Virtual Environment". When you install, it is installing
# on a project basis in this venv folder under the lib > python > packages
#import heroes
#print(heroes)

# There used to be a python 2 but people wanted to new features, so they created python 3
# But python 3 is not backwards to python 2
# Python 3 is the future, but there are a lot of existing python 2
# Virtual Environments help us install the features we need. Since we have a venv for each project, we install and know it is compatible with that version
# So it doesn't matter when things change versions, because you know you have everything installed for that project


#import villains
import random

screen = Screen()
screen.colormode(255)
# can also use color mode on the turtle library

tim = Turtle()
tim.shape("circle")
tim.color("IndianRed2")

# Turtle Challenge 1
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# Turtle Challenge 2
# for i in range(10):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)

def set_random_color(turtle):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.pencolor((r, g, b))

# Turtle Challenge 3
# for num_sides in range(3, 11):
#
#     set_random_color(tim)
#
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(360/num_sides)


# Turtle Challenge 4 (Random walk)

# ANGLES = [0, 90, 180, 270]
#
# def random_walk():
#
#     tim.width(10)
#     tim.speed(10)
#
#     for i in range(100):
#         set_random_color(tim)
#         tim.setheading(random.choice(ANGLES))
#         tim.forward(25)
#
# random_walk()

# Challenge 5
# Tuple is an ordered list (1, 4, 5)
# Tuple is FINAL (doesn't allow changes)

# Challenge 6 Spirograph
def draw_spirograph():
    tim.speed("fastest")

    # Loop through 60 times, with a space between each circle as 6
    # 60 * 6 = 360 (full circle)
    for i in range(60):
        print(i)
        set_random_color(tim)
        tim.circle(100, None, 100)
        tim.right(6)

draw_spirograph()



screen.exitonclick()