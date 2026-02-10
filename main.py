from tkinter import *
import pandas as pd
import random


df = pd.read_csv("./data/spanish500.csv")
data = df.to_dict(orient="records")


#Constants
BACKGROUND_COLOR = "#B1DDC6"


#Methods
def new_word():
    global selection
    selection = random.choice(data)
    spanish_word = selection["Spanish"]
    canvas.itemconfig(word, text=spanish_word)
    canvas.itemconfig(title, text="Spanish")

def flip_card():
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=selection["English"])

#Window Setup
window = Tk()
window.title("Learn Spanish")
window.configure(background=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
window.attributes("-topmost", True)
window.after(3000, func=flip_card)

#Import Images
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
#Canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
#Buttons
right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=new_word)
wrong_button = Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=new_word)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

new_word()







window.mainloop()