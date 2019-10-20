import unittest
import TicTacToe


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe.TicTacToe(3)

    def test_something(self):
        self.assertEqual(self.game.move(1, 1), 0)
        self.assertEqual(self.game.move(1, 1), -1)

if __name__ == '__main__':
    unittest.main()
