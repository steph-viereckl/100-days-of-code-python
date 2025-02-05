from flask import Flask
from random import randint
from random import choice

app = Flask(__name__)
number_to_guess = randint(0,9)

def is_correct(function):
    def wrapper_function(*args):
        if args[0] == number_to_guess:
            return True
        else:
            return False

    return wrapper_function

# This decorator function will check to see what webpage the user is at. If they are on the homepage (i.e. www.google.com/) then it will run this
@app.route("/")
def welcome_page():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media3.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.webp?cid=ecf05e47obfo9ejq8u3ml9ww0sakjiy5wor1bsvg52frdtfx&ep=v1_gifs_search&rid=giphy.webp&ct=g' "
            "alt='Retro looking numbers 1-9' width='500' height='600'>")

@app.route("/<int:user_guess>")
def check_guess(user_guess):

    list_of_colors = ["Aquamarine", "CornflowerBlue", "DeepPink", "LightSeaGreen"]
    random_color = choice(list_of_colors)

    if user_guess > number_to_guess:
        return (f"<h1 style='color:{random_color}'>Too High!</h1>"
                f"<img src='https://media2.giphy.com/media/12zgyJya7QwQKI/giphy.webp?cid=790b7611wbtgoulqx98s5ejv4x4bctigyn5z4kc0vl78dxql&ep=v1_gifs_search&rid=giphy.webp&ct=g' alt='Jim Carrey with pokies in his face saying uh oh'>")
    elif user_guess < number_to_guess:
        return (f"<h1 style='color:{random_color}'>Too Low!</h1>"
                f"<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2J0Z291bHF4OThzNWVqdjR4NGJjdGlneW41ejRrYzB2bDc4ZHhxbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8YEeD1WB5FeyAiONoe/giphy.webp' alt='Girl saying yikes'>")
    else:
        return (f"<h1 style='color:{random_color}'>User guessed correctly</h1>"
                f"<img src='https://media2.giphy.com/media/JQFuCdFbQAbNaawknQ/200.webp?cid=790b76118skjgrnn019d8qnw3xnly6sp073ymlk26iirf4sz&ep=v1_gifs_search&rid=200.webp&ct=g' alt='Guy shimmying in celebration'>")

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
