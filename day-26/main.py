import random
numbers = [1, 2, 3]
new_list = []

for num in numbers:
    add_1 = num + 1
    new_list.append(add_1)

# List comprehension
# new_list = [new_item for item in list]

# The first part of list comprehension is what you are doing to each item in the list
# In this case, we are taking num plus 1 and it replaces in the new list
new_list = [num + 1 for num in numbers]


# List comprehension works with all sequence
# Sequences = list, range, string, tuple
# It will always go in order and do something with it
name = "Stephanie"
letters_in_name = [letter for letter in name]
print(letters_in_name)

# Challenge - range(1, 5)
# Loop through range where each of the numbers in the range is doubled
doubled_numbers = [num * 2 for num in range(1,5)]
print(doubled_numbers)

# Conditional list comprehension to add a condition
# Only add new_item if the test passes
# new_list = [new_item for item in list if test]

names = ["Alex", "James", "Naomi", "Amos", "Bobbie"]

updated_names = [name for name in names if len(name) <= 4]
cap_names = [name.upper() for name in names if len(name) > 4]

print(updated_names)
print(cap_names)

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# student_score = {
#     "Alex": 90,
#     "James": 99
# }

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passing_scores = {student: score for (student, score) in student_scores.items() if score > 60}
print(student_scores.items())
print(passing_scores)

# Using pandas and dictionary comprehnsion on data frams
# Remember, to loop through dictionary:
student_dict = {
    "student": ["Ron", "Harry", "Hermoine"],
    "score": [78, 79, 100]
}

for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through data frame
for (key, value) in student_data_frame.items():
    # This will tell you the name of the column
    print(key)
    # All the data in each column
    print(value)

for (index, row) in student_data_frame.iterrows():
    # Number value
    print(index)
    # Row is student: Hermoine, score: 100
    print(row)
    # Print out just the student
    print(row.student)
    print(row.score)