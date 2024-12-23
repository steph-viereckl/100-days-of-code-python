# with open("file_that_doesnt_exist.txt") as file:
#     file.read()
    # This will get an error: FileNotFoundError: [Errno 2] No such file or directory: 'file_that_doesnt_exist.txt'
    # When this exception is thrown

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

# IndexError
# fruit_list = ["orange", "banana"]
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)

# Exceptions:
# Try - Try something that might fail
# Except - Do this is if there is an exception
# Else - Do this is if there isn't an exception
# Finally - Do this no matter what

# Let's add an exception

# try:
#     file = open("file_that_doesnt_exist.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sfasd"])
# # Should never use a bare except - that is too generic. We don't know which error is going to happen
# except FileNotFoundError:
#     # Create it if it doesn't exist
#     file = open("file_that_doesnt_exist.txt", "w")
#     file.write("something in the file")
# except KeyError as error_message:
#     print(f"Here is the error message: {error_message}")
# else:
#     print('This runs if the try is successful')
# # This is optional
# finally:
#     file.close()
#     print("file was closed")
#
#     # I can throw a built in exception
#     raise KeyError("This is the message that will show")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
# If user puts in a crazy height, we can raise our own exception