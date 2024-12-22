from tkinter import *

DEFAULT_EMAIL = "email@email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    new_password = f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n"

    # mode = "a" is append (add to it)
    with open("password_data.txt", mode="a") as file:
        file.write(new_password)

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