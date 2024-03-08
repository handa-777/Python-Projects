from tkinter import *
from time import sleep
from tkinter import ttk, messagebox

FONT = ("Courier", 20)
GREEN = "#9bdeac"
RED = "#e7305b"
countdown = None


def count_up():
    for i in range(0, 300):
        progressbar.step(1)
        progressbar.update()
    end_writing(True)


def start_app():
    user_input.focus()
    count_up()
    start_timer(5)


def is_writing(event):
    global countdown
    window.after_cancel(countdown)
    timer.config(text="5 secs")
    start_timer(5)


def start_timer(count):
    global countdown
    if count >= 0:
        timer.config(text=f"{count} secs")
        countdown = window.after(1000, start_timer, count - 1)
    else:
        end_writing(False)


def end_writing(is_success):
    if is_success:
        messagebox.showinfo(message="Congratulations! You succeeded in writing for 5 minutes.")
    else:
        messagebox.showinfo(message="You failed to write for 5 minutes. Try again!")


def reset_app():
    pass


window = Tk()
window.title("The Most Dangerous Writing")
window.minsize(width=900, height=800)

progressbar = ttk.Progressbar(window, maximum=300, length=900)
progressbar.grid(column=0, row=0, columnspan=2)

title_label = Label(text="The Most Dangerous Writing", font=FONT)
title_label.grid(column=0, row=1, pady=10, columnspan=2)

user_input = Text(width=70, height=30, font=FONT)
user_input.grid(column=0, row=2, pady=15, padx=15, columnspan=2)

start_button = Button(text="Start", command=start_app)
start_button.grid(column=0, row=3)

timer = Label(text="5 secs", font=FONT)
timer.grid(column=1, row=3)

user_input.bind("<Key>", is_writing)

window.mainloop()
