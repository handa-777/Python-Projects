from flask import Flask
import random

rand_num = random.randint(0, 9)
print(rand_num)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route('/<int:num>')
def guess_number(num):
    if num == rand_num:
        return ("<h1 style='color: green'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")
    elif num < rand_num:
        return ("<h1 style='color: red'>Too low, try again</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
    else:
        return ("<h1 style='color: purple'>Too high, try again</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")


if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run(debug=True)