from tkinter import *
# This is not a class in tkinter, it's another module
from tkinter import messagebox
import random

DEFAULT_EMAIL = "email@email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Invalid Entry", message="One or more fields is empty. Please try again.")
    else:

        valid = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\n"
                                                      f"Email: {email}\n"
                                                      f"Password: {password}\n\n"
                                                      f"Click OK to save.")

        if valid:

            new_entry = f"{website} | {email} | {password}\n"

            # mode = "a" is append (add to it)
            with open("password_data.txt", mode="a") as file:
                file.write(new_entry)

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
website_input = Entry(width=39)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

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