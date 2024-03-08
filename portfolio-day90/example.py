from tkinter import *
import random, math
from words import words_list, correct_scores

FONT = ("Courier", 20)
X_CORDS = [110, 250, 390]
Y_CORDS = [23, 53, 85]
GREEN = "#9bdeac"
RED = "#e7305b"
TOTAL = 0
WRONG = 0
i = 0
timer = None
current_words = []


def generate_random_words():
    canvas.delete("all")
    current_words.clear()
    for y in Y_CORDS:
        for x in X_CORDS:
            new_word = random.choice(words_list)
            current_words.append(new_word)
            canvas.create_text(x, y, text=new_word, font=FONT)


def typing(event):
    global TOTAL, WRONG, i
    user_input = my_input.get()
    TOTAL += 1
    if user_input != current_words[i]:
        WRONG += 1
    i += 1
    if i == 9:
        i = 0
        generate_random_words()
    my_input.delete(0, END)


def reset_timer():
    global TOTAL, WRONG
    window.after_cancel(timer)
    timer_label.config(text="01:00")
    TOTAL = 0
    WRONG = 0
    total_label.config(text=f"Total: {TOTAL}")
    correct_label.config(text=f"Correct: {TOTAL - WRONG}")
    wrong_label.config(text=f"Wrong: {WRONG}")
    best_label.config(text=f"Best Score: {max(correct_scores)}")


def start_timer():
    count = 1 * 60
    count_down(count)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_label.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        show_result()


def show_result():
    global TOTAL, WRONG
    correct = TOTAL - WRONG
    total_label.config(text=f"Total: {TOTAL}")
    correct_label.config(text=f"Correct: {correct}")
    wrong_label.config(text=f"Wrong: {WRONG}")
    correct_scores.append(correct)
    best_label.config(text=f"Best Score: {max(correct_scores)}")
    TOTAL = 0
    WRONG = 0


window = Tk()
window.title("Typing Speed Test App")
window.config(pady=50, padx=40)

title_label = Label(text="Typing Speed Test", font=("Courier", 50))
title_label.grid(column=0, row=0, columnspan=3)

best_label = Label(text=f"Best Score: {max(correct_scores)}", fg=GREEN, font=("Courier", 15))
best_label.grid(column=0, row=1, pady=10)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

timer_label = Label(text="01:00", fg=GREEN, font=("Courier", 40))
timer_label.grid(column=1, row=2)

canvas = Canvas(window, width=500, height=100, bg='white')
canvas.grid(column=0, row=3, columnspan=3)

generate_random_words()

my_input = Entry(width=12, font=FONT)
my_input.grid(column=1, row=4, ipady=3, pady=15)
my_input.bind('<Return>', typing)

total_label = Label(text="Total: 0", font=("Courier", 20))
total_label.grid(column=0, row=5)

correct_label = Label(text="Correct: 0", fg=GREEN, font=("Courier", 30))
correct_label.grid(column=1, row=5)

wrong_label = Label(text="Wrong: 0", fg=RED, font=("Courier", 20))
wrong_label.grid(column=2, row=5)

window.mainloop()
