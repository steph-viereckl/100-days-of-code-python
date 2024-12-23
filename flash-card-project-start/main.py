from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


def mark_incorrect():
    pass

def mark_correct():
    pass

# Window
window = Tk()
window.title("Steph's Flashcard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Front
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
# Need to define the x position and y position (to center image)
canvas.create_image(400, 263, image = card_front_img)
canvas.grid(column=1, row=0, columnspan=3)

# Incorrect Button
incorrect_button = Button(text="Start", command=mark_incorrect, highlightbackground=BACKGROUND_COLOR)
incorrect_button.grid(column=0, row=1)

# Correct Button
start_button = Button(text="Start", command=mark_correct, highlightbackground=BACKGROUND_COLOR)
start_button.grid(column=3, row=1)

window.mainloop()