from flask import Flask
import random
app = Flask(__name__)

# __name__ is a Special Attribute. If name
print(__name__) # returns __main__

# We are running this from the current file where the app code is located, and we aren't using an imported module
print(random.__name__)

# This decorator function will check to see what webpage the user is at. If they are on the homepage (i.e. www.google.com/) then it will run this
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# This will only run if the user is at the checkout page
@app.route("/checkout")
def check_out():
    return "<p>Check out page</p>"

if __name__ == "__main__":
    print("This means we are running from the current file")
    # This does the same thing as flask run in the terminal. This allows us to run as if we did from the terminal
    # Then we can use the stop button to stop it instead of Ctrl + C
    app.run()




# To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is with the --app option
# This will tell the framework what the name of the file is that contains our server
# Terminal > export FLASK_APP=hello.py

# Make sure your terminal is in the correct directory
# To run: flask --app hello run
# To quit: Control + C

# What is the @ mean? Python Decorator