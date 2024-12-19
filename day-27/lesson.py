# import tkinter
# Or we can import every class so we don't have to write out tkinter every time
from tkinter import *

def button_click():
    label.config(text=input_text.get())

# Create window
window = Tk()
window.title("My first GUI Program")
# window will scale to fit everything in it, but if it is empty or doesn't have much you can set min size
window.minsize(width=500, height=300)

# Label
label = Label(text="I AM LABEL", font=("Arial", 24, "bold"))
# "The Packer" packs the label and places it into the screen and automatically center
# The packer is a geometric management layout system. It has options like which side to pack to,
label.pack()
# label.pack(side="left")
# This is how we change attributes for something we have created
label["text"] = "New Label"
label.config(text = "Hello Label")

# Button
button = Button(text="Click Me", command=button_click)
button.pack()

# Entry (Input box)
input_text = Entry(width=10)
input_text.pack()

# There are different Layout managers
# 1. Pack (Pack widgets next to each outer, starting from top to bottom by default). If you do pack side = left, it will pack from left to right
# 2. Place (Precise positioning - provide an x and y value) good if you only have a few widgets
# label.place(x=0, y=0)
# 3. Grid (imagines entire program is a grid, and you can define rows and columns.
# label.grid(column=0, row=0) this will be the top left corner
# Grid is relative to other components. So you need to think about the order

# You can't mix grid and pack in the same program















# While loop to keep screen open and so it can listen. In the past we created a while loop to do that
# while True:
# This is included as mainloop(). It always has to be at the end.
window.mainloop()
