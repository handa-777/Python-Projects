from tkinter import *


def button_clicked():
    user_input = int(my_input.get())
    to_km = user_input * 1.609
    result.config(text=str(to_km))


window = Tk()
window.title("My First GUI Program")
window.minsize(width=220, height=80)

my_input = Entry(width=10)
my_input.grid(column=1, row=0)

mile = Label(text="Miles")
mile.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
