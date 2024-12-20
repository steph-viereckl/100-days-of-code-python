from tkinter import *

def convert_to_km():
    converted_km = float(mile_input.get()) * 1.609
    km_output.config(text=converted_km)

# Create window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Input box for miles
mile_input = Entry(width=10)
mile_input.insert(END, string="0")
mile_input.grid(column=1, row=0)

# Miles Label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# "Is equal to" label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Km output Label
km_output = Label(text="0")
km_output.grid(column=1, row=1)

# Km output Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=convert_to_km)
button.grid(column=1, row=2)

window.mainloop()
