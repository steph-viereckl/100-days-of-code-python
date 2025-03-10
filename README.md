# 100 Days of Code (Python)

### Days Completed: 69 🎉 Days Remaining: 31

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

# Installing Requirements

You can create a file with your `requirements.txt` and then use `pip install -r ./requirements.txt` to install them

# Flask URL Paths

## Variable Path
A Variable path is what is typed into the url. We can then grab that vasriable

```python
@app.route('/greeting/<name>')
def show_greeting(name):
    return f"The name is: {name}"

@app.route('/age/<int:num>')
def show_age(num):
    return f"The age is: {num}"

```

## POST Request with Flask Server

We can recieve data entered by user using Flask. Once form is submitted, we can catch the POST request in our server. To do this, we need an input in our form using the `name` attribute
```html
<form action="{{ url_for('login') }}" method="post">
      <label for="name">Name</label>
      <input type="text" id="name" name="name" placeholder="Name">
      <label for="password">Password</label>
      <input type="text" id="password" name="password" placeholder="Password">
      <input type="submit" value="Ok">
    </form>
```

The `name` attribute identifies what data point you are going to get from the form

```python
from flask import Flask, render_template, request

@app.route('/login', methods=['POST'])
def login_page():
    print(f'name: {request.form["name"]}')
    print(f'password: {request.form["password"]}')

    return render_template("login.html", name=request.form["name"])

```

## WTF Forms

We saw that when using a basic HTML form, we can use the request object from Flask to access the key-value pairs that were entered into the form when the POST request was made.

With WTForms, it's even easier to get hold of the form data. All you have to do is to tap into the

`<form_object>.<form_field>.data`

```html
{% extends "base.html" %}
{% from 'bootstrap5/form.html' import render_form %}
{% block title %}Login{% endblock %}
{% block content %}
    <div class="container">
    <h1>Login</h1>
        {{ render_form(form) }}
    </div>
{% endblock %}
```

```python
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

```

# Git & Version control

## Terminal Commands

`ls -a` shows hidden files like `.git`
`touch file_name.txt` creates files
`mkdir` creates a folder 
`clear` clears the terminal
`open -a /Applications/Visual\ Studio\ Code.app file-name.txt` to open 

1. Create file
2. `git init` initializes a Git repo
   3. "Working Directory" is the top folder
4. Need to add to staging area. `git status` tells us what is staged.
5. `git add file_name.txt` adds to the staging area
   6.   `git add .` adds everything inside the working directory
6. `git commit -m "Message"` creates a commit 
   7. Git messages are always written in present test. "Complete Chapter 1" instead of "Completed Chpater 1"
8. `git log` shows commit history
   9.    `HEAD --> master` shows where you currently are at
10. `git diff chapter3.txt` to see differences
    11. This will help you determine whether you just need to
12. `git checkout chapter3.txt` will roll back to last version that was committed
13. `git rm --cached -r .` remove everything from the staging area

## Remote Repositories

Use GitHub 

1. Need to tell computer that you want to add a remote repo

`git remote add origin https://github.com/steph-viereckl/Story.git`

`origin` is the remote repository and can be called anything but that is the convention.

`git push -u origin main` pushes the local repo to the remote using the `u` flag to link up.

### .GitIgnore

`.gitignore` 

DS Store files are settings files, for example, how you like to have your files shown (i.e. in a grid)

1. Create a new file called `.gitignore` (must be exactly typed)
2. Use `ls -a` to see hidden files
```txt
.DS_Store
.gitignore
secrets.txt

# There are certain rules in the .gitignore

# You can also use wildcard, for example to ignore all .txt files
*.txt
```

## Git Clone

Pull down from remote to your own local working directory. You make a copy on your on environment

## VSCODE Python

Python > Create Environment > Venv > Install requirements