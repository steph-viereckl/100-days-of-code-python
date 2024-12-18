from os.path import split

import pandas

# TODO Convert csv to dictionary where key is letter and value is the word
# TODO Create list of phonetic code words from the input of a user and it returns a list with the words


user_input = input("What word do you need to spell with the NATO alphabet?").upper()
split_word = list(user_input)
# print(split_word)
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data_frame)

# Convert data frame into dictionary using dictionary comprehension
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

# Convert data frame into dictionary using for loop
# for (index, row) in nato_data_frame.iterrows():
#     nato_dict[row.letter] = row.code

return_list = []

for letter in split_word:
    if letter in nato_dict:
        return_list.append(nato_dict[letter])

# Return inputted word in a list format i.e. Hi = ["Hotel", "India"]
print(f"Nato Codes: {return_list}")
