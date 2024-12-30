from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

def mark_incorrect():
    word_label.config(text=random.choice(french_words)["French"])

def mark_correct():
    word_label.config(text=random.choice(french_words)["French"])


word_data_frame = pandas.read_csv("data/french_words.csv")
french_words = word_data_frame.to_dict(orient="records")
print(french_words)

# Window
window = Tk()
window.title("Steph's Flashcard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Front
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
# Need to define the x position and y position (to center image)
canvas.create_image(400, 263, image = card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Title Label
title_label = Label(text="French", font=("Arial", 40, "italic"), bg="white")
title_label.place(x=400, y=150, anchor=CENTER)

# Title Label
word_label = Label(text=random.choice(french_words)["French"], font=("Arial", 60, "bold"), bg="white")
word_label.place(x=400, y=263, anchor=CENTER)

# Incorrect Button
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_img, command=mark_incorrect, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
incorrect_button.grid(column=0, row=1)

# Correct Button
correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, command=mark_correct, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)

window.mainloop()