from tkinter import *

def button_click():
    label.config(text=input_text.get())

# Create window
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
label = Label(text="I AM LABEL", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

# Button
button = Button(text="Button", command=button_click)
button.grid(column=1, row=1)

# Button
new_button = Button(text="New Button", command=button_click)
new_button.grid(column=2, row=0)

# Entry (Input box)
input_text = Entry(width=10)
input_text.grid(column=3, row=3)












# While loop to keep screen open and so it can listen. In the past we created a while loop to do that
# while True:
# This is included as mainloop(). It always has to be at the end.
window.mainloop()
