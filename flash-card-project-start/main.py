from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
MILLISECONDS = 3000
timer = None
current_words = {}

def mark_incorrect():
    pass

def mark_correct():
    pass

def get_words():
    global current_words
    current_words = random.choice(word_dict)

def set_front():
    pass

def show_card(is_front):

    if is_front is True:
        get_words()
        card_front_img = PhotoImage(file="images/card_front.png")
        canvas.create_image(400, 263, image=card_front_img)
        title_label.config(text="French")
        word_label.config(text=current_words["French"])

    else:
        title_label.config(text="English")
        word_label.config(text=current_words["English"])


def count_down(is_front):
    print("In count down")
    show_card(is_front)

    global timer
    timer = window.after(MILLISECONDS, count_down, not is_front)

# Read CSV File
word_data_frame = pandas.read_csv("data/french_words.csv")
word_dict = word_data_frame.to_dict(orient="records")

# Window
window = Tk()
window.title("Steph's Flashcard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Front
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
# Need to define the x position and y position (to center image)
canvas.create_image(400, 263, image = card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# TODO need to dynamically set front image and then switch it 

# Title Label
title_label = Label(font=("Arial", 40, "italic"), bg="white")
title_label.place(x=400, y=150, anchor=CENTER)

# Title Label
word_label = Label(font=("Arial", 60, "bold"), bg="white")
word_label.place(x=400, y=263, anchor=CENTER)

# Incorrect Button
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_img, command=mark_incorrect, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
incorrect_button.grid(column=0, row=1)

# Correct Button
correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, command=mark_correct, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)

# Select the card to show
# count_down(True)

window.mainloop()