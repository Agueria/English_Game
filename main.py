from tkinter import Tk, Canvas, PhotoImage, Button
import pandas as pd
import random

class FlashyApp:
    def __init__(self):
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.current_card = {}
        self.to_learn = {}
        self.load_data()

        # Initialize Tkinter window
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)

        # Flip card timer
        self.flip_timer = self.window.after(3000, self.flip_card)

        # Initialize canvas and UI elements
        self.init_canvas()
        self.init_buttons()

        self.next_card()
        self.window.mainloop()

    def load_data(self):
        try:
            self.to_learn = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
        except FileNotFoundError:
            original_data = pd.read_csv("data/french_words.csv")
            self.to_learn = original_data.to_dict(orient="records")

    def next_card(self):
        self.current_card = random.choice(self.to_learn)
        self.update_card("French", self.current_card["French"], "black", self.card_front_img)
        self.flip_timer = self.window.after(3000, self.flip_card)

    def flip_card(self):
        self.update_card("English", self.current_card["English"], "white", self.card_back_img)

    def update_card(self, title, word, fill_color, card_image):
        self.window.after_cancel(self.flip_timer)
        self.canvas.itemconfig(self.card_title, text=title, fill=fill_color)
        self.canvas.itemconfig(self.card_word, text=word, fill=fill_color)
        self.canvas.itemconfig(self.card_background, image=card_image)

    def is_known(self):
        self.to_learn.remove(self.current_card)
        new_data = pd.DataFrame(self.to_learn)
        new_data.to_csv("data/words_to_learn.csv", index=False)
        self.next_card()

    def init_canvas(self):
        self.canvas = Canvas(width=800, height=526)
        self.card_front_img = PhotoImage(file="images/card_front.png")
        self.card_back_img = PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas.config(bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

    def init_buttons(self):
        cross_image = PhotoImage(file="images/wrong.png")
        self.unknown_button = Button(image=cross_image, highlightthickness=0, command=self.next_card)
        self.unknown_button.grid(row=1, column=0)

        check_image = PhotoImage(file="images/right.png")
        self.known_button = Button(image=check_image, highlightthickness=0, command=self.is_known)
        self.known_button.grid(row=1, column=1)

if __name__ == "__main__":
    app = FlashyApp()
