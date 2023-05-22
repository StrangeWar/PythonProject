from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        string = function()
        bold_string = f'<b>{string}</b>'
        return bold_string
    return wrapper


def make_italic(function):
    def wrapper():
        string = function()
        bold_string = f'<em>{string}</em>'
        return bold_string
    return wrapper


def make_underline(function):
    def wrapper():
        string = function()
        bold_string = f'<u>{string}</u>'
        return bold_string
    return wrapper


@app.route('/')
@make_bold
@make_italic
@make_underline
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<img src="https://media3.giphy.com/media/Cmr1OMJ2FN0B2/200w.webp?cid=ecf05e475tengghkid8r6lzwl26yrvuwf7bdfozpnmd03e36&rid=200w.webp&ct=g">' \
           '<img src="https://media2.giphy.com/media/3A3PvQtjS0oyA/giphy.webp?cid=ecf05e47vrr3ecdd6uous8yy7e16bjl50zpap0w1jtifcaue&rid=giphy.webp&ct=g">'


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:age>")
def greeting(name, age):
    return f"Hello {name} your age is {age}."


if __name__ == '__main__':
    # Run the code in debug mode to auto-reload
    app.run(debug=True)
