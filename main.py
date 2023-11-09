from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Reading CSV file
try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('spanish_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def word_change():
    global current_card, card_flip_timer
    window.after_cancel(card_flip_timer)
    current_card = random.choice(to_learn)
    picked_words = current_card['Spanish']
    canvas.itemconfig(language, text='Spanish', fill='black')
    canvas.itemconfig(card_words, text=picked_words)
    canvas.itemconfig(canvas_image, image=card_front_image)
    card_flip_timer = window.after(3000, func=change_side)


def change_side():
    translation = current_card['English']
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(card_words, text=translation)
    canvas.itemconfig(canvas_image, image=card_back_image)


def known_word():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('words_to_learn.csv', index=False)
    word_change()


window = Tk()
window.title('Flash Cards App')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


card_flip_timer = window.after(3000, func=change_side)


# Images
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
# card_back_image = PhotoImage(file='images/card_back.png')
# canvas.create_image(card_back_image)
card_front_image = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_back_image = PhotoImage(file='images/card_back.png')


language = canvas.create_text(400, 150, text='Title', fill='black', font=('Arial', 40, 'italic'))
card_words = canvas.create_text(400, 263,text='Word', fill='black', font=('Arial', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=wrong_image, highlightthickness=0, command=word_change)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0,  command=known_word)
right_button.grid(row=1, column=1)




word_change()



window.mainloop()

