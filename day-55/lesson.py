from flask import Flask

app = Flask(__name__)

# __name__ is a Special Attribute. If name
print(__name__) # returns __main__

# This decorator function will check to see what webpage the user is at. If they are on the homepage (i.e. www.google.com/) then it will run this
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# This will only run if the user is at www.example.com/bye
@app.route("/bye")
def check_out():
    return "<p>Check out page</p>"

# We can add variable sections to a URL by marking it with this syntax: <variable_name>
# Then our function can receive the variable name and we can use it within our function
# Flask is going to turn whatever comes after username/ into a variable called "name"
@app.route("/hello/<name>")
def greet(name):
    # Dynamically render based upon what the user typed into the url*
    return f"Hello {name}!"

# We can also use a variable converter to convert to path... or an int or string
@app.route("/username/<path:name>")
def greet_with_converter(name):
    # Dynamically render based upon what the user typed into the url*
    # If I type in /username/stephanie/1234 then "stephanie/1234" will be returned
    return f"Hello {name}!"

# We can also use multiple variables
@app.route("/username/<name>/<int:number>")
def multiple_variables(name, number):
    # Dynamically render based upon what the user typed into the url*
    # If I type in /username/stephanie/1234 then "stephanie/1234" will be returned
    return f"Hello {name} this is your {number}!"


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)

# Debug mode: off --> NEED TO STOP AND REFRESH SERVER FOR CHANGES TO APPEAR
# Debug mode: on --> activate debugger to identify issues, activates automatic reloader (without having to start and stop server)
