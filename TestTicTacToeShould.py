import unittest
from TicTacToe import TicTacToe, Game, Board

class TestTicTacToeShould(unittest.TestCase):

    def test_return_true_if_position_is_A1(self):
        game = Game()
        input = "A1"
        self.assertEqual(game.check_valid_positions(input), True)

    def test_return_true_if_position_is_A2(self):
        game = Game()
        input = "A2"
        self.assertEqual(game.check_valid_positions(input), True)

    def test_return_true_if_position_is_A3(self):
        game = Game()
        input = "A2"
        self.assertEqual(game.check_valid_positions(input), True)

    def test_return_true_if_position_is_B1(self):
        game = Game()
        input = "A2"
        self.assertEqual(game.check_valid_positions(input), True)

    def test_return_true_if_position_is_B2(self):
        game = Game()
        input = "A2"
        self.assertEqual(game.check_valid_positions(input), True)

    def test_return_true_if_position_is_B3(self):
        game = Game()
        input = "A2"
        self.assertEqual(game.check_valid_positions(input), True)

    def test_return_true_if_position_is_C1(self):
        game = Game()
        input = "A2"
        self.assertEqual(game.check_valid_positions(input), True)

    def test_return_true_if_position_is_C2(self):
        game = Game()
        input = "A2"
        self.assertEqual(game.check_valid_positions(input), True)

    def test_return_true_if_position_is_C3(self):
        game = Game()
        input = "A2"
        self.assertEqual(game.check_valid_positions(input), True)

    def test_check_incorrect_input_player(self):
        game = Game()
        input = "NB"
        self.assertEqual(game.check_valid_positions(input), False)

    def test_put_chip_into_board(self):
        board = Board()
        position = "A1"
        board.set_chip(position=position)
        self.assertEqual(board.board[0][0], "X")

    def test_check_position_alreay_taken(self):
        board = Board()
        position = "A1"
        board.set_chip(position=position)
        self.assertEqual(board.check_position_taken(position), True)

    def test_return_false_if_position_is_not_taken(self):
        board = Board()
        position_taken = "A1"
        position_not_taken = "B1"
        board.set_chip(position=position_taken)
        self.assertEqual(board.check_position_taken(position_not_taken), False)

    def test_return_true_if_all_positions_are_taken(self):
        board = Board()
        board.board = [
            ["X","O","X"],
            ["O","X","O"],
            ["X","O","X"]
        ]
        self.assertEqual(board.check_board_is_all_completed(), True)

    def test_return_false_if_all_position_are_not_taken(self):
        board = Board()
        board.board = [
            ["X", " ", "X"],
            ["O", "X", "O"],
            ["X", "O", "X"]
        ]
        self.assertEqual(board.check_board_is_all_completed(), False)

if __name__ == '__main__':
    unittest.main()
