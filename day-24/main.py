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
with open("my_file.txt") as file:

    contents = file.read()
    print(contents)
