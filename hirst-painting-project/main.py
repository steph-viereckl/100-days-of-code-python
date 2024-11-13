import colorgram
import turtle
import random
# extracted_colors = colorgram.extract("hirst.jpg", 10)
# color_list = []
#
# for i in extracted_colors:
#
#     color_list.append((i.rgb.r, i.rgb.b, i.rgb.g))
#
# print(color_list)

color_list = [(199, 117, 175), (124, 24, 36), (210, 213, 221), (168, 57, 106), (222, 227, 224), (186, 53, 158), (6, 83, 57), (109, 85, 67), (113, 175, 161), (22, 174, 122), (64, 138, 153), (39, 36, 36), (76, 48, 40), (9, 47, 67), (90, 53, 141), (181, 79, 96), (132, 42, 40), (210, 151, 200)]

# 10 by 10 row of dots
# 20 in size spaced apart by 50

screen = turtle.Screen()
turtle.colormode(255)

artsy_turtle = turtle.Turtle()
artsy_turtle.penup()
artsy_turtle.hideturtle()
artsy_turtle.setheading(225)

print(f'heading: {artsy_turtle.heading()}')
artsy_turtle.forward(250)
artsy_turtle.setheading(0)
print(f'position: {artsy_turtle.position()}')

y_position = artsy_turtle.xcor()
x_position = artsy_turtle.ycor()

for row in range(10):

    for column in range(10):

        artsy_turtle.dot(20, random.choice(color_list))
        artsy_turtle.forward(50)

    y_position += 50
    artsy_turtle.setposition(x_position, y_position)

screen.exitonclick()