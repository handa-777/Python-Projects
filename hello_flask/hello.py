from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
@make_underline
@make_emphasis
def bye():
    return "bye"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
