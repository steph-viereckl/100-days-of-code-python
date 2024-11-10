# https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
import prettytable

# To install package... PyCharm > Settings > Click on Project > Python Interpreter > "+" > Find package and install

# Create object/instance from class
table = prettytable.PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
