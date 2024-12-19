
# Advanced Python Arguments
# We have already done keyword arguments...
def my_keyword_function(a, b, c):
    print(a, b, c)

# In a keyword argument, you specify the parameters and can call anyway you want if you have keyword in front
my_keyword_function(c=3, a=1, b=2)

# But what if when I can this the arguments typically have default values? You can define that way!
def my_advanced_function(a=1, b=2, c=3):
    print(a + b + c)

# Now I can call it without specifying the parameters
my_advanced_function()

# But I can also overwrite the parameter if needed
my_advanced_function(a=4)

# Unlimited Arguments in functions
# * is important but "args" is just standard naming practice
# def add(*args):
#     for n in args:
#         print(n)


# "Unlimited Positional Arguments" because the x number of arguments will be ordered
def add(*args):
    # args is a Tuple so we can use the sum() function. We can also use index functionality
    return sum(args)

print(add(1,4,5, 5))

# "Many Keyworded Arguments"
def calculate(**kwargs):
    # kwarg is basically a dictionary
    # {'add': 3, 'multiple': 5}
    print(kwargs)

    # We can look through the dictionary passed to the function
    for key, value in kwargs.items():
        print(key)
        print(value)

    # Or if we know the name, we can access it direction
    print(kwargs["add"])

calculate(add=3, multiple=5)

def calculate2(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


calculate2(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        # If we access arguments like this they are required. It will crash without
        # self.make = kw["make"]
        # self.model = kw["model"]
        # If we access arguments like this they are optional
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Honda", model="Prius")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")


def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)
# 4 (7, 3, 0) {'x': 10, 'y': 64}

all_aboard(4, 7, 3, 0, x=10, y=64)
# 4 (7, 3, 0) {'x': 10, 'y': 64}