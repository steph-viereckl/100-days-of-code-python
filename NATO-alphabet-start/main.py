from calendar import error
from os.path import split

import pandas

# TODO Convert csv to dictionary where key is letter and value is the word
# TODO Create list of phonetic code words from the input of a user and it returns a list with the words

def generate_phonetic_word():

    user_input = input("What word do you need to spell with the NATO alphabet?").upper()
    nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
    # Convert data frame into dictionary using dictionary comprehension
    nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

    try:
        # Convert data frame into dictionary using for loop
        # for (index, row) in nato_data_frame.iterrows():
        #     nato_dict[row.letter] = row.code

        return_list = [nato_dict[letter] for letter in user_input]

    except KeyError as error_message:

        print(f"Invalid entry {error_message}. Sorry, only letters in the alphabet please.")
        generate_phonetic_word()

    else:

        # Return inputted word in a list format i.e. Hi = ["Hotel", "India"]
        print(f"Nato Codes: {return_list}")

generate_phonetic_word()