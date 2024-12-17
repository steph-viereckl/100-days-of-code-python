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
print(updated_names)