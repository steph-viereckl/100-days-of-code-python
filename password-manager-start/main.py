from tkinter import *
# This is not a class in tkinter, it's another module
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

DEFAULT_EMAIL = "email@email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def find_password():

    website = website_input.get()

    try:
        with open("password_data.json", mode="r") as data_file:

            # Convert existing JSON into pictionary
            password_dict = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title=f"Password File Empty", message=f"No passwords have been added yet.")

    else:

        # Preference is to use if/else to catch issues. But if you can't easily do an if/else.. an exception is better
        # Exceptions should be occasional.
        try:
            password_entry = password_dict[website]
            print(f"password_entry: {password_entry}")
        except KeyError:
            messagebox.showwarning(title=f"Website Not Found", message=f"No password found for {website}")
        else:
            messagebox.showinfo(title=f"{website}", message=f"{website}\n"
                                                            f"Email: {password_entry["email"]}\n"
                                                            f"Password: {password_entry["password"]}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    password_list += [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(numbers) for i in range(randint(2, 4))]
    password_list += [choice(symbols) for i in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)

    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":

        messagebox.showwarning(title="Invalid Entry", message="One or more fields is empty. Please try again.")

    else:
        new_entry = f"{website} | {email} | {password}\n"

        # mode = "a" is append (add to it)
        # mode = "w" is to write (if file doesn't exist, it will create it)
        # mode = "r" is read mode

        try:
            with open("password_data.json", mode="r") as data_file:

                # Read existing JSON file
                # load() takes json and converts it into a python dictionary
                data = json.load(data_file)

        except FileNotFoundError as message:

            with open("password_data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:

            # Update old data with new data
            data.update(new_data)

            with open("password_data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            # Reset form
            website_input.delete(0, END)
            email_input.delete(0, END)
            email_input.insert(0, DEFAULT_EMAIL)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
# Need to define the x position and y position (to center image)
canvas.create_image(100, 100, image = lock_img)
canvas.grid(column=1, row=0)
# canvas.grid(column=1, row=1)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website Input
website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

# Website Search Button
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

# Email/Username Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Email Input
email_input = Entry(width=39)
email_input.insert(0, DEFAULT_EMAIL)
email_input.grid(column=1, row=2, columnspan=2)

# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password Input
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()