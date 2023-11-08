from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flash Cards App')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Images
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
# card_back_image = PhotoImage(file='images/card_back.png')
# canvas.create_image(card_back_image)
card_front_image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front_image)

language_text = canvas.create_text(400, 150, text='Title', fill='black', font=('Arial', 40, 'italic'))
spanish_words = canvas.create_text(400, 263, text='word', fill='black', font=('Arial', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)
window.mainloop()

