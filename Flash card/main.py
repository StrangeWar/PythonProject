import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
words_list = {}
current_card = {}
# __________________________________________Data________________________________________________________________________
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_list = original_data.to_dict(orient="records")
else:
    words_list = df.to_dict(orient="records")


def is_known():
    words_list.remove(current_card)
    data = pandas.DataFrame(words_list)
    data.to_csv("data/words_to_learn.csv", index=False)

    new_card()


# ______________________________________Generating new flash card_______________________________________________________

def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# _________________________________________________UI___________________________________________________________________

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 265, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 265, text="", fill="black", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

check_button_img = PhotoImage(file="./images/right.png")
check_button = Button(image=check_button_img, command=is_known, highlightthickness=0, borderwidth=0)
check_button.grid(column=0, row=1)

cross_button_img = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_button_img, command=new_card, highlightthickness=0, borderwidth=0)
cross_button.grid(column=1, row=1)

new_card()

window.mainloop()
