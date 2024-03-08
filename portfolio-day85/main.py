from tkinter import *
from PIL import Image, ImageDraw, ImageFont


def insert_watermark(user_pic, user_wm):
    img = Image.open(user_pic)
    width, height = img.size

    draw = ImageDraw.Draw(img)

    text = user_wm

    font_size = 30
    font = ImageFont.truetype('Arial', font_size)

    x = width/3*2
    y = height/3*2 + 50

    draw.text((x, y), text, fill='white', font=font)

    img.show()

    img.save("cat_watermakr.jpg")


def button_clicked():
    picture = pic_input.get()
    text = wm_input.get()
    print(picture, text)
    insert_watermark(picture, text)


window = Tk()
window.title("My WaterMark App")
window.minsize(width=300, height=300)

pic_adr = Label(text="Picture Address: ")
pic_adr.grid(column=0, row=0)

pic_input = Entry(width=10)
pic_input.grid(column=1, row=0)

wm_text = Label(text="WaterMark Text: ")
wm_text.grid(column=0, row=1)

wm_input = Entry(width=10)
wm_input.grid(column=1, row=1)

button = Button(text="Insert", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
