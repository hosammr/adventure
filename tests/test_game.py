import unittest

from game import Game


class GameTest(unittest.TestCase):
    def test_create(self):
        game = Game(name="Testgame")
        self.assertEqual(str(game), "Testgame")

    def test_load_simple(self):
        game = Game.load("data/simple_game.json")
        self.assertEqual(str(game), "Simple game")
        self.assertEqual(len(game.locations), 1)
        self.assertIn("woonkamer", game.locations)
        self.assertEqual(str(game.location), "woonkamer")

    def test_load_test(self):
        game = Game.load("data/test_game.json")
        self.assertEqual(str(game), "Test game")
        self.assertEqual(len(game.locations), 3)
        self.assertIn("keuken", game.locations)
        self.assertEqual(str(game.location), "keuken")
