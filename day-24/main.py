# # Built in open method
# file = open("my_file.txt")
#
# # Returns the contents of the file as a string
# contents = file.read()
# print(contents)
#
# # Need to close the file so that we don't keep taking up computer resources
# # It is kind of like keeping a ton of tabs open
# file.close()

# BUT if you open it with the following syntax it will manage opening/closing for you
# Default mode is read only
# mode = "w" is writable (overwrite)
# mode = "a" is append (add to it)
with open("my_file.txt", mode="a") as file:

    file.write("Hello")

# If you are in write mode and try to edit a file that doesn't exist, it will create it
# Here is an absolute file path (starting with drive)
# with open("/Users/sviereckl/Desktop/new_file.txt", mode="w") as file_2:
#     file_2.write("Hello again")

# /Users/sviereckl/Documents/GitHub/100-days-of-code/day-24/main.py

# Here is a relative file path (starting with current position)
with open("../../../../Desktop/new_file.txt", mode="w") as file_2:
    file_2.write("Hello from relative path")

# Recap
# Open and read (default)
# Open and overwrite (w)
# Open and append (a)