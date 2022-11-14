from tkinter import *
import requests
from datetime import datetime

# TEXT FOR INSPIRATIONAL QUOTES
def get_quote():
    response = requests.get(url="https://zenquotes.io/api/random")
    all_info = response.json()
    quote = all_info[0]['q'] + " " + all_info[0]['a']
    canvas.itemconfig(quote_text, text=quote, fill="white")

window = Tk()
window.title("Inspirational Quote of the Day...")
window.config(padx=20, pady=20)

canvas = Canvas(width=400, height=800)
background_img = PhotoImage(file="back.png")
canvas.create_image(200, 400, image=background_img)
quote_text = canvas.create_text(200, 400, text="Click the pink lotus for a new quote!", width=350, font=("Verdana", 30), fill="white")
canvas.grid(row=0, column=0)

flower_img = PhotoImage(file="flower.png")
flower_button = Button(image=flower_img, highlightthickness=0, command=get_quote)
flower_button.grid(row=0, column=1)


window.mainloop()
