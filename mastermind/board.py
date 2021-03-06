#!/usr/bin/env python3

from collections import Counter
from mastermind.player import Player
from mastermind.history import History
from mastermind.utils.num_validator import NumValidator
from random import randint
import requests
from typing import List


class Board:
    """
    Board class.
    """

    def __init__(self, difficulty: int, num_list: List[int],
                 dev_mode: bool = False):
        """
        Board constructor.
        Default value for the amount of numbers to guess is 4. If board
        values are passed in, it will be used. Otherwise, numbers will be
        generated with API or locally depending on whether developer mode
        is on or not.
        """
        self.num_count = 4
        self.num_combinations = 9 if difficulty == 4 else 7
        if num_list:
            self.num_list = num_list
        else:
            if dev_mode:
                self.num_list = self.generate_numbers_locally()
            else:
                self.num_list = self.generate_numbers_with_API()
        self.history = History(self.num_count)
        self.hints_remaining = [i for i in range(self.num_count)]

    def generate_numbers_locally(self) -> List[int]:
        """
        Generates random numbers using the random libary.
        """
        return [randint(0, self.num_combinations)
                for i in range(self.num_count)]

    def generate_numbers_with_API(self) -> List[int]:
        """
        Generates random numbers using the random.org API. If for any reason
        the call is unsuccessful, numbers will be generated locally.
        """
        url = "https://www.random.org/integers/"
        query_string = {"num": "4", "min": "0",
                        "max": str(self.num_combinations),
                        "col": "1", "base": "10", "format": "plain",
                        "rnd": "new"}
        print("Generating board...")
        try:
            response = requests.request(
                "GET", url, params=query_string, timeout=5)
        except Exception:
            print("Connection timed out. Generating numbers locally...")
            return self.generate_numbers_locally()
        else:
            if response.status_code == 200:
                return [int(n) for n in
                        response.text.split("\n") if len(n)]
            print(
                f"{response.status_code} status code from API call."
                "Generating numbers locally...")
            return self.generate_numbers_locally()

    def get_player_input(self, player: Player):
        """
        Ask current player for guess input. Will only accept valid integers.
        """
        guesses = []
        guess_count = 1
        nv = NumValidator()
        print(f"\n{player.turns} turns left.")
        print(f"Please enter a number between 0 and {self.num_combinations}.\n"
              "Use 'h' for a hint. Caution, this will affect your\n"
              "total score!\n")
        while len(guesses) != self.num_count:
            guess = nv.get_guess(
                guess_count, 0, self.num_combinations)
            if guess == -1:
                self.generate_hint()
                continue
            guesses.append(guess)
            guess_count += 1
        player.turns -= 1
        self.history.player_guesses.append(guesses)

    def check_board(self):
        """
        Validates user input with correct numbers.
        Algorithm speed is currently O(n) time complexity and O(n) space
        complexity.
        """
        last_guesses = self.history.player_guesses[-1]
        correct_colors = sum(
            (Counter(self.num_list) & Counter(last_guesses)).values())
        correct_positions = 0
        for i in range(len(last_guesses)):
            if last_guesses[i] == self.num_list[i]:
                correct_positions += 1
                correct_colors -= 1
        new_entry = {"correct_colors": correct_colors,
                     "correct_positions": correct_positions}
        self.history.player_scores.append(new_entry)
        return new_entry

    def display_history(self):
        """
        Displays the current history of the player's guesses and scores.
        Also displays the legend.
        """
        print(self.history)
        print("\nX = Correct number, correct location\n"
              "O = Correct number, incorrect location\n"
              "* = Incorrect number, incorrect location")

    def generate_hint(self) -> bool:
        """
        Generates a hint for the user. Returns True if there are hints
        available, False if not.
        """
        if not len(self.hints_remaining):
            print("No hints remaining!\n")
            return False
        r = randint(0, len(self.hints_remaining) - 1)
        random_index = self.hints_remaining.pop(r)
        num = self.num_list[random_index]
        print(f"{num} is at position {random_index + 1}.\n")
        return True
