from tkinter import *
import pandas as pd

df = pd.read_csv("./data/spanish500.csv")
data = df.to_dict(orient="records")
print(data[0]["Spanish"])

#Constants
BACKGROUND_COLOR = "#B1DDC6"

#Methods
def new_word():
    pass

#Window Setup
window = Tk()
window.title("Learn Spanish")
window.configure(background=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
window.attributes("-topmost", True)


#Import Images
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

#Buttons
right_button = Button(image=right_img, borderwidth=0, highlightthickness=0)
wrong_button = Button(image=wrong_img, borderwidth=0, highlightthickness=0)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

#Canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)








window.mainloop()