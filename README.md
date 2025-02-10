# 100 Days of Code (Python)

### Days Completed: 53 🎉 Days Remaining: 47

___

## Best Practices

- When using methods you didn't write, use keyword parameters so it is clear what you are passing to the method
- If you only need 1 or 2 items from an imported module, use `import module_name`
  - But if you are going to be using many items from that module, be specific using the `from module_name import xyz, abc` so that you don't have to use `module_name.something` all the time
- Don't do `from module import *` because it might be confusing where you get items from
- All method names and variable names should use snake case (`hello_world`)
- All class names should use Pascal Case (`HelloWorld`)

## Class Inheritence 

```python

class Fish(Animal):

    def __init__(self):
        super().__init__()
```

The `Fish` Class inherits from the `Animal` class. To do this, pass in the `Animal` class to the `Fish` class and include `super().__init__()` in the constructor


## File Paths

### Absolute File Path
This is the file path starting from the root directory `/`

`/Stephanie/Documents/GitHub/blah-blah-blah`

### Relative File Path
This is the file path from the working directory, the location from which we are currently working from. To indicate the file path of the current folder, use a `./`

### Moving Directories
To move up in a directory use a dot `.`

For example, to move up a folder and navigate into Desired Folder you would use `../Desired_Folder/file.txt`

To move up 2 folders, do `../../Desired_Folder/file.txt`

To reference something in the same folder, you can do `./file.txt` or shorthand of `file.txt`

## Sending Email

```python
import smtplib
import os
# pip install python-dotenv
from dotenv import load_dotenv

# Object from smtp class to connect to specific provider
with (smtplib.SMTP("smtp.gmail.com") as connection):

    load_dotenv()
    # These are stored in the .env file
    from_email = os.environ.get("FROM_EMAIL", "From Email cannot be found")
    email_password = os.environ.get("PASSWORD", "Email password cannot be found")

    subject_line = f"Subject: Here is the subject line!\n\n"
    message = f"Here is the message in the body of the email"
    combined_message = subject_line + message
    # Was running into issues with encoding so ignoring some chars
    # updated_message = combined_message.encode('ascii', 'ignore').decode('ascii')
    connection.starttls()
    connection.login(user=from_email, password=email_password)
    connection.sendmail(from_addr=from_email,to_addrs=from_email,msg=combined_message.encode("utf-8"))
```

## Open File

```python
with open("file-path.txt", mode="r") as data:
    letter = data.read()
```

## Create new file

```python
new_file = "hello world"

with open("movies-to-watch.txt", "w") as file:
    file.write(new_file)
```

## Web Scraping

```python
from bs4 import BeautifulSoup
import requests

# Get full header here: # https://myhttpheader.com/
header = {
    "Accept-Language":"en-US",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}

response = requests.get(url="www.google.com", headers=header)
website_html = response.text

soup = BeautifulSoup(markup=website_html, features="html.parser")
# Find span where class is...
price = soup.find(name="span", class_="a-price-whole").getText()
decimal = soup.find(name="span", class_="a-price-fraction").getText()
movie_title_tags = soup.find_all(name="h3", class_="title")
# Find tag where element is inside an li tag, and is an h3 element with an id of "title-of-a-story"
song_tags = soup.select("li h3#title-of-a-story")

```

# Special Attributes

There are special attributes like `__name__` that are reserved.

`__name__` will tell you whether you are running the code directly from the file or from another module. 

# Python Decorators

Seen in more advanced Python projects. Decorator function is a function that is going to give additional functionality to an existing function.
```python
## ********Day 54 Start**********
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()
```

Decorator function is just a function that wraps another function and gives that function some additional functinality.
```python
import time

def say_hello():
    time.sleep(2)
    print("Hello")

# Lets say we always wanted a little delay
say_hello()
```

But what if we wanted to add this sleep delay for many greetings? We would have to repeat it. Or...

```python
import time

def say_hello():
    time.sleep(2)
    print("Hello")

def say_bye():
    time.sleep(2)
    print("Bye")

say_hello()
say_bye
```

Or we could use a decorator function. 

```python
import time

def delay_decorator(function):
    
  def wrapper_function():
    time.sleep(2)
    # Do something before you run the function
    function()
    # Or do something after you run the fucntion  
    function() # Or run it again! 
      
  return wrapper_function()

@delay_decorator
def say_hello():
    time.sleep(2)
    print("Hello")
    
@delay_decorator
def say_bye():
    time.sleep(2)
    print("Bye")

say_hello()
say_bye()
```

The `@` sign is syntactic sugar. We could also just call the name of the decorator
```python
decorated_function = delay_decorator(say_hello)
decorated_function()
```

## Advanced Decorator Fnctions

https://replit.com/@appbrewery/python-advanced-decorators#main.py

```python
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):

  def wrapper(*args, **kwargs):
    if args[0].is_logged_in == True:
        # Trigger function if user is logged in
        function(args[0])
  return wrapper

@is_authenticated_decorator
# Positional argument at 0
def create_blog_post(user):
    print(f"This is the blog post by {user.name}")

new_user = User("Stephanie")
create_blog_post(new_user)
```

```python
# Unlimited Positional Arguments
def my_function(*args):
    for item in args:
        print(item)

my_function(1,2,3,4,5)

# Unlimited Keyword Arguments
def my_function(**kwargs):
    x = kwargs.get("n1")
    y = kwargs.get("n2")
    print(f"X cord is {x} and Y cord is {y}")

my_function(n1= 12.4546, n2=-111.11111)
```

### Another example

```python
# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")

        # Must use *args here. args will return a tuple
        result = function(*args)
        print(f"It returned: {result}")
        
    return wrapper

# TODO: Use the decorator 👇

@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)
```

# Web Development

Go to Chrome DevTools > Console > `document.body.contentEditable=true` and you can edit directly on the website. Save webpage html

# Bootstrap

* `none` is for very narrow phones (<576px)
* `sm` is for mobile (>576px)
* `md` is for iPads (>768px)
* `lg` is for laptops (>992px)
* `xl` is for desktops (>1200px)
* `xxl` is for tvs (>1400px)