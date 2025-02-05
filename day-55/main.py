from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        text = function()
        return f"<b>{text}</b>"
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        text = function()
        return f"<i>{text}</i>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        text = function()
        return f"<u>{text}</u>"
    return wrapper_function


# This decorator function will check to see what webpage the user is at. If they are on the homepage (i.e. www.google.com/) then it will run this
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Here are using additional decorators
@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
