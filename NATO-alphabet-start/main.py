from os.path import split

import pandas

# TODO Convert csv to dictionary where key is letter and value is the word
# TODO Create list of phonetic code words from the input of a user and it returns a list with the words


user_input = input("What word do you need to spell with the NATO alphabet?").upper()
split_word = list(user_input)
print(split_word)
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_data_frame)
nato_list = []

return_list = []

for letter in split_word:
    row = nato_data_frame[nato_data_frame.letter == letter]
    return_list.append(row.code)

print(return_list)