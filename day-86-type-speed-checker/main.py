from tkinter import *
from faker import Faker
from random_word import RandomWords, Wordnik

LIGHT_TEAL = "#E0F1EB"
TEAL = "#C2E4D7"
DARK_TEAL = "#4D5B56"
RED = "#FF0000"

# with open("sample.txt", mode="r") as data:
#     sample_text = data.read()
#     word_list = sample_text.split()

start_word_index = 0
end_word_index = 7
score = 0
seconds_remaining = 60
start_timer = False
word_list = []
current_words = []
words_to_show = None

#--------------- Functions -------------------#

def get_word_list():

    global word_list
    global start_word_index
    global end_word_index

    start_word_index = 0
    end_word_index = 7

    fake = Faker()
    word_list = fake.words(200)

    show_words()

def next_word():
    global start_word_index
    global end_word_index

    # Advance the index so we get a new set of words
    start_word_index += 1
    end_word_index += 1

    show_words()

def show_words():
    global current_words

    # Get the next set of words from word list
    current_words = word_list[start_word_index:end_word_index]
    updated_text = " ".join(current_words)

    # Update Entry Box
    word_box.config(text=updated_text)

def increase_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

def clear_word():
    input_text.delete(first=0, last="end")

def count_down():

    global seconds_remaining
    # Reset the seconds remaining block
    seconds_remaining -= 1
    # Update the label
    timer_label.config(text=f"{seconds_remaining} Seconds")

    # If there is time left, then wait a second and then count down again by 1 second
    if seconds_remaining > 0:
        window.after(1000, count_down)
    if seconds_remaining == 0:
        timer_label.config(text=f"{seconds_remaining} Seconds")
        timeout()

def timeout():
    # Disable the text box
    input_text.config(state="disabled")
    # Show the timeout label
    timeout_label.config(text=f"Times Up! Final WPM: {score}")
    timeout_label.grid(row=4, column=2)
    # Show the Reset Button
    reset_button.grid(row=5, column=2)


def reset():
    global seconds_remaining

    # Clear the last word typed, remove the time out label and reset button
    clear_word()
    timeout_label.grid_forget()
    reset_button.grid_forget()

    # Reset list of words
    get_word_list()

    # Enable the text box and reset the time
    input_text.config(state="normal")
    seconds_remaining = 60
    timer_label.config(text=f"{seconds_remaining} Seconds")

def on_keystroke(event):

    # On the first keystroke, start timer
    if seconds_remaining == 60:
        count_down()

    # Get users input
    typed_letters = input_text.get()

    # If the User enters the correct word, score a point and reset input box
    if typed_letters == current_words[0]:
        increase_score()
        clear_word()
        next_word()

    # If User has backspaced and there is no input, just do nothing
    elif not typed_letters:
        pass

    # If the User enters a space, reset input box
    elif typed_letters[-1] == " ":
        clear_word()

#--------------- UI -------------------#

window = Tk()
window.title("Typing Speed Assessment")
window.config(padx=200, pady=50, bg=TEAL)

# Title Label
label = Label(text="How Fast Can You Type?", bg=TEAL, fg=DARK_TEAL, font=("Arial", 50, "normal"))
label.grid(row=0, column=0, columnspan=5)

# Score
score_label = Label(text=f"Score: {score}", bg=TEAL, fg=DARK_TEAL, font=("Arial", 20, "bold"), anchor="w")
score_label.grid(row=1, column=1)

# Timer
timer_label = Label(text="60 Seconds", bg=TEAL, fg=DARK_TEAL, font=("Arial", 20, "bold"), justify="left")
timer_label.grid(row=1, column=3, pady=10)

# Sample Text To Write
word_box = Label(text=words_to_show, bg=LIGHT_TEAL, fg=DARK_TEAL, font=("Arial", 20, "normal"), wraplength=500)
word_box.grid(row=2, column=2, pady=10)

get_word_list()

# Entry Text Box
input_text = Entry(width=20)
input_text.bind("<KeyRelease>", on_keystroke)
input_text.focus()
input_text.grid(row=3, column=2)

# Timeout Text (Initially hidden)
timeout_label = Label(text=f"Times Up! Final WPM: {score}", bg=TEAL, fg=RED, font=("Arial", 25, "normal"))

# Reset Button (Initially hidden)
reset_button = Button(text="Reset", command=reset, highlightbackground=TEAL)

window.mainloop()