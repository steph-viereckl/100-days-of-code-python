from tkinter import *
import math

# Event Driven GUI is driven through "mainloop()". It is basically looping through every millisecond to see if something has happened
# So if we have another loop in our program (i.e. a while loop) it won't be able to get to the mainloop(). So we need to do something differently
# TKinter has a method called after(). It takes the amount of time it should wait, and then after that time, it calls the function and you can pass in arguments

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
MILLISECONDS = 100
SECONDS_IN_MIN = 1
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
checkmarks = ""

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_session_seconds = WORK_MIN * SECONDS_IN_MIN
    short_break_seconds = SHORT_BREAK_MIN * SECONDS_IN_MIN
    long_break_seconds = LONG_BREAK_MIN * SECONDS_IN_MIN

    if reps % 2 == 1:
        count_down(work_session_seconds)
        timer_label.config(text="Work Work Work", fg=GREEN)
    elif reps <= 6:
        count_down(short_break_seconds)
        timer_label.config(text="Short break", fg=PINK)
    else:
        count_down(long_break_seconds)
        timer_label.config(text="Long break", fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global checkmarks
    minutes = math.floor(count / 60)
    seconds = count % 60

    # Because of dynamic typing, we can change the data type of a variable
    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        window.after(MILLISECONDS, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks += "✓"
            counter_label.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# def example():
#     pass
#
# # After method runs after the mainloop is called
# # 1000 milliseconds = 1 second
# # after(time to elapse, function to call, unlimited arguments to pass to function)
# window.after(1000, example)

# Timer Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
timer_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Need to define the x position and y position (to center image)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

# Checkmark Counter
counter_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "normal"))
counter_label.grid(column=1, row=3)

window.mainloop()