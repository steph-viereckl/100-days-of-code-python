import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_NAME = "Courier"

window = Tk()
window.title("Watermark 4 U")
window.config(padx=50, pady=50, bg=YELLOW)

def upload_file():
    global img_file_path

    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected Photo: {file_path}")
        root.destroy()
        img_file_path = file_path

def add_watermark():

    global img_file_path

    print(f"Add watermark to {img_file_path}")
    photo = Image.open(img_file_path)
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    # font = ImageFont.truetype("arial.ttf", 40)
    # font = ImageFont.load("arial.pil")

    myfont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 200)
    # font = ImageFont.load_default()
    text = watermark_text.get()
    drawing.text((100,100), text, fill=black, font=myfont)
    photo.show()
    new_img_path = "img/new_photo.png"
    photo.save(new_img_path)


# ---------------------------- UI SETUP ------------------------------- #

img_file_path = ""

# Watermark Label
watermark_label = Label(text="Watermark 4 U", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
watermark_label.grid(row=0, column=2, columnspan=2)

# Select File Button
select_button = Button(text="Select File", command=upload_file, highlightbackground=YELLOW)
select_button.grid(row=1, column=2, columnspan=2, pady=25)

# Watermark Text Input
watermark_text = Entry(width=25)
watermark_text.focus()
watermark_text.grid(row=4, column=2, pady=25)

# Add Watermark Button
watermark_button = Button(text="Add Watermark", command=add_watermark, highlightbackground=YELLOW)
watermark_button.grid(row=4, column=3)

window.mainloop()