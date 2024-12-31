from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
MILLISECONDS = 3000
timer = None
current_words = {}
is_front = True

######################## Functions ########################

def mark_incorrect():

    # Cancel current timer (and a new one will start in count down)
    window.after_cancel(timer)
    count_down(show_front=True)

def mark_correct():

    global word_data_frame
    global word_dict

    # Remove the current word from the data frame
    word_data_frame = word_data_frame[word_data_frame["French"] != current_words["French"]]
    # Update words to learn CSV
    word_data_frame.to_csv("words_to_learn.csv", index=False)
    # Update the list that is being used show the words
    word_dict = word_data_frame.to_dict(orient="records")

    # Cancel current timer (and a new one will start in count down)
    window.after_cancel(timer)
    count_down(show_front=True)

def show_front_card():
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_words["French"], fill="black")

def show_back_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_words["English"], fill="white")

def count_down(show_front):

    global timer, current_words

    if show_front:
        # Reset current word
        current_words = random.choice(word_dict)

        show_front_card()
    else:
        show_back_card()

    timer = window.after(MILLISECONDS, count_down, not show_front)

######################## Program Start ########################

# Read CSV File
try:
    words_to_learn_df = pandas.read_csv("words_to_learn.csv")

# The first time this program is run we don't have the words to learn file
except FileNotFoundError:
    print('File not found')
    word_data_frame = pandas.read_csv("data/french_words.csv")
    word_data_frame.to_csv("words_to_learn.csv", index=False)
    word_dict = word_data_frame.to_dict(orient="records")
else:
    word_dict = words_to_learn_df.to_dict(orient="records")

# Window
window = Tk()
window.title("Steph's Flashcard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Front
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)

canvas_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))

# Need to define the x position and y position (to center image)
canvas.grid(column=0, row=0, columnspan=2)

# Incorrect Button
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_img, command=mark_incorrect, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
incorrect_button.grid(column=0, row=1)

# Correct Button
correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, command=mark_correct, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)

# Select the card to show
count_down(show_front=True)

window.mainloop()