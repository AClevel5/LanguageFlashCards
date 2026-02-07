from tkinter import *

#Constants
BACKGROUND_COLOR = "#B1DDC6"

#Window Setup
window = Tk()
window.title("Learn Spanish")
window.configure(background=BACKGROUND_COLOR)
window.config(padx=40, pady=40)
window.attributes("-topmost", True)


#Import Images
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

#Buttons
right_button = Button(image=right_img, highlightthickness=0)
wrong_button = Button(image=wrong_img, highlightthickness=0)

canvas = Canvas(width=500, height=400, bg=BACKGROUND_COLOR)
canvas.create_image(200, 200, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)






window.mainloop()