"""
Project: tests_rpsls_game.py
Author: E Wilber
Last date modified: {12-11-23}

Unittests for Project: rpsls_game.py
"""
import unittest
import tkinter as tk
from tkinter import messagebox

#code for Rock Paper Scissors Lizard Spock game (rpsls_game.py)
class RockPaperScissorsLizardSpock:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors, Lizard, Spock")
        self.create_widgets()

    def create_widgets(self):
        # Player 1 label and dropdown
        player1_label = tk.Label(self.root, text="Player 1:")
        player1_label.grid(row=0, column=0)
        self.player1_var = tk.StringVar(self.root)
        self.player1_var.set("Rock")  # Default choice
        player1_dropdown = tk.OptionMenu(self.root, self.player1_var, "Rock", "Paper", "Scissors", "Lizard", "Spock")
        player1_dropdown.grid(row=0, column=1)

        # Player 2 label and dropdown
        player2_label = tk.Label(self.root, text="Player 2:")
        player2_label.grid(row=1, column=0)
        self.player2_var = tk.StringVar(self.root)
        self.player2_var.set("Rock")  # Default choice
        player2_dropdown = tk.OptionMenu(self.root, self.player2_var, "Rock", "Paper", "Scissors", "Lizard", "Spock")
        player2_dropdown.grid(row=1, column=1)

        # Button to determine the winner
        play_button = tk.Button(self.root, text="Play", command=self.on_click)
        play_button.grid(row=2, columnspan=2)

    def determine_winner(self, player1, player2):
        rules = {
            'Rock': ['Scissors', 'Lizard'],
            'Paper': ['Rock', 'Spock'],
            'Scissors': ['Paper', 'Lizard'],
            'Lizard': ['Spock', 'Paper'],
            'Spock': ['Scissors', 'Rock']
        }

        if player1 not in rules or player2 not in rules:
            raise ValueError("Invalid choice! Please select again.")

        if player1 == player2:
            return "It's a tie!"

        if player2 in rules[player1]:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

    def on_click(self):
        player1_choice = self.player1_var.get()
        player2_choice = self.player2_var.get()

        result = self.determine_winner(player1_choice, player2_choice)
        messagebox.showinfo("Result", result)

#The Unittests
class TestRockPaperScissorsLizardSpock(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.game = RockPaperScissorsLizardSpock(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_invalid_choice(self):
        with self.assertRaises(ValueError):
            self.game.determine_winner("Invalid", "Choice")

    def test_player1_wins(self):
        result = self.game.determine_winner("Rock", "Scissors")
        self.assertEqual(result, "Player 1 wins!")

    def test_player2_wins(self):
        result = self.game.determine_winner("Paper", "Scissors")
        self.assertEqual(result, "Player 2 wins!")

    def test_tie(self):
        result = self.game.determine_winner("Scissors", "Scissors")
        self.assertEqual(result, "It's a tie!")

if __name__ == "__main__":
    unittest.main()






