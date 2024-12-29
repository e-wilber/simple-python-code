"""
Project: guessing_game.py
Author: E Wilber
Last date modified: {11-21-23}

Random number guessing game.
"""
import random
import tkinter as tk
from tkinter import messagebox

MAX = 20
BUTTON_WIDTH = 2

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.guess_buttons = []
        for i in range(1, MAX+1):
            guess_button = tk.Button(master, text=str(i), width=BUTTON_WIDTH, state="disabled",
                                     command=lambda i=i: self.make_guess(i))
            guess_button.grid(row=(i-1)//5, column=(i-1)%5)
            self.guess_buttons.append(guess_button)

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.grid(row=(MAX-1)//5+1, column=0, columnspan=5)
        self.guessed_list = []

        self.reset_game()

    def start_game(self):
        self.secret_number = random.randint(1, MAX)
        self.reset_game()
        self.enable_guess_buttons()

    def reset_game(self):
        self.guesses = 0
        self.guess_label_var = tk.StringVar(value="Guesses: 0")
        self.guess_label = tk.Label(self.master, textvariable=self.guess_label_var)
        self.guess_label.grid(row=(MAX-1)//5+2, column=0, columnspan=5)

        self.guessed_list = []
        for guess_button in self.guess_buttons:
            guess_button.config(state="disabled")

    def enable_guess_buttons(self):
        for guess_button in self.guess_buttons:
            guess_button.config(state="normal")

    def disable_guess_button(self, guess):
        self.guess_buttons[guess-1].config(state="disabled")

    def add_guess(self, guess):
        self.guessed_list.append(guess)

    def make_guess(self, guess):
        self.guesses += 1
        self.guess_label_var.set("Guesses: {}".format(self.guesses))

        if guess == self.secret_number:
            messagebox.showinfo("Winner!", "Congratulations, you guessed the number!")
            self.start_game()
        else:
            self.add_guess(guess)
            self.disable_guess_button(guess)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()