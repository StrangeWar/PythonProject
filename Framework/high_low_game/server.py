import random

from flask import Flask

app = Flask(__name__)
random_number = random.randint(0, 9)
print(random_number)


@app.route("/")
def guess_number():
    return '<h1>Guess a number between 0-9.</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def guess(number):

    if number > 9:
        return f"<h1>You entered out of range.</h1>"
    elif random_number == number:
        return f"<h1 style='text-color: green'>You found me!</h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number < random_number:
        return f"<h1 style='text-color: red'>Too low! Try again.</h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > random_number:
        return f"<h1 style='text-color: blue'>Too High! Try again.</h1>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == '__main__':
    # Run the code in debug mode to auto-reload
    app.run(debug=True)
