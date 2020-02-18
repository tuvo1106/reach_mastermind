#!/usr/bin/env python3

from mastermind.player import Player
from mastermind.history import History
import unittest


class Player_Test(unittest.TestCase):
    """
    Tests for the Player class.
    """

    def test_check_victory_truthy(self):
        """
        Test check_victory() for truthy returns.
        """
        history = History()
        history.player_scores = [
            {"correct_colors": 0, "correct_positions": 4}]
        player = Player("Tu", "1")
        self.assertTrue(player.check_victory(4, history))

    def test_check_victory_falsy(self):
        """
        Test check_victory() for falsy returns.
        """
        history = History()
        history.player_scores = [
            {"correct_colors": 1, "correct_positions": 3}]
        player = Player("Tu", "1")
        self.assertFalse(player.check_victory(4, history))
        history.player_scores = [
            {"correct_colors": 2, "correct_positions": 2}]
        self.assertFalse(player.check_victory(4, history))
        history.player_scores = [
            {"correct_colors": 3, "correct_positions": 1}]
        self.assertFalse(player.check_victory(4, history))
        history.player_scores = [
            {"correct_colors": 4, "correct_positions": 0}]
        self.assertFalse(player.check_victory(4, history))

    def test_check_defeat_truthy(self):
        """
        Test check_defeat() for truthy returns.
        """
        player = Player("Tu", "2")
        player.turns = 0
        self.assertTrue(player.check_defeat())

    def test_check_defeat_falsy(self):
        """
        Test check_defeat() for falsy returns.
        """
        player = Player("Tu", "2")
        self.assertFalse(player.check_defeat())
        player.turns = 2
        self.assertFalse(player.check_defeat())
        player.turns = 1
        self.assertFalse(player.check_defeat())


if __name__ == '__main__':
    unittest.main()
