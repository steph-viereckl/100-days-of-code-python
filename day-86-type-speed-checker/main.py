# TODO Build GUI that shows user text. Allow user to type in word
# TODO Create timer that runs for 60 seconds
# Keep track of user entering in words and whether they got it right or wrong
# Space bar advances to the next word? Backspace goes back words?

from tkinter import *
from faker import Faker

TEAL = "#C2E4D7"
DARK_TEAL = "#4D5B56"
file_path = f"sample.txt"

# cookie_baker = Faker()
# print(f"word: {cookie_baker.word()}")

# TODO Instead of a static piece of text, create dynamic word list
with open("sample.txt", mode="r") as data:
    sample_text = data.read()

word_list = sample_text.split()

start_word_index = 0
end_word_index = 15

current_words = word_list[start_word_index:end_word_index]
words_to_show = " ".join(current_words)
print(f"Words to show: {words_to_show}")

#--------------- Functions -------------------#

def next_word():
    global current_words
    global start_word_index
    global end_word_index

    # Advance the indexs so we get a new set of words
    start_word_index += 1
    end_word_index += 1

    # Get the next set of words from word list
    current_words = word_list[start_word_index:end_word_index]
    updated_text = " ".join(current_words)

    # Update Entry Box
    word_box.config(text=updated_text)

def get_user_input(event):

    typed_letters = input_text.get()
    print(f"typed_letters: {typed_letters}")
    print(f"current_words[0]: {current_words[0]}")

    # If the User enters the correct word, score a point and reset input box
    if typed_letters == current_words[0]:
        input_text.delete(first=0, last="end")
        next_word()

    # If the User enters a space, reset input box
    elif typed_letters[-1] == " ":
        input_text.delete(first=0, last="end")

#--------------- UI -------------------#

window = Tk()
window.title("Typing Speed Assessment")
window.config(padx=200, pady=200, bg=TEAL)

# Label
label = Label(text="How Fast Can You Type?", bg=TEAL, fg=DARK_TEAL, font=("Arial", 50, "normal"))
label.grid(row=0, column=0)

# Sample Text To Write
word_box = Label(text=words_to_show, bg=TEAL, fg=DARK_TEAL, font=("Arial", 20, "normal"))
word_box.grid(row=1, column=0, pady=10)

# Entry Text Box
input_text = Entry(width=25)
input_text.bind("<KeyRelease>", get_user_input)
input_text.focus()
input_text.grid(row=3, column=0)

window.mainloop()