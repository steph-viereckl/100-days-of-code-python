with open("file_that_doesnt_exist.txt") as file:
    file.read()
    # This will get an error: FileNotFoundError: [Errno 2] No such file or directory: 'file_that_doesnt_exist.txt'
    # When this exception is thrown

# KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existing_key"]

# IndexError
fruit_list = ["orange", "banana"]
fruit = fruit_list[3]

# TypeError
text = 'abc'
print(text + 5)

# Exceptions:
# Try
# Except
# Else
# Finally