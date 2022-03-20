#Kamil Salawa 20/03/2022
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

#<GUI-------------------------------------------->
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)


canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

red_button = PhotoImage(file="images/wrong.png")
green_button = PhotoImage(file="images/right.png")
wrong_button = Button(image=red_button, highlightthickness=0)
right_button = Button(image=green_button, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)




title = Label(text="Title")


window.mainloop()