#Kamil Salawa 20/03/2022
from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image= card_back)

def is_known():
    to_learn.remove(current_card)
    # print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


#<GUI-------------------------------------------->
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

red_button = PhotoImage(file="images/wrong.png")
green_button = PhotoImage(file="images/right.png")
wrong_button = Button(image=red_button, highlightthickness=0, command=next_card)
right_button = Button(image=green_button, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)


next_card()

window.mainloop()