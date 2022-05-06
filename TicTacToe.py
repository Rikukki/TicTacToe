class TicTacToe:
    def Fake(self, value: int) -> int:
        return 1

class Board:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def set_chip(self, position: str, chip: str):
        x_dict = {
            "A": 0,
            "B": 1,
            "C": 2
        }
        x = x_dict[position[:-1]]
        y = int(position[1]) - 1
        self.board[x][y] = chip

    def check_position_taken(self, position: str):
        x_dict = {
            "A": 0,
            "B": 1,
            "C": 2
        }
        x = x_dict[position[:-1]]
        y = int(position[1]) - 1
        return self.board[x][y] != " "

    def check_board_is_all_completed(self):
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == " ":
                    return False
        return True

    def check_if_there_is_a_winner(self):
        return


class Game:

    def check_valid_positions(self, input):
        correct_positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        return input in correct_positions



if __name__ == '__main__':
    board = Board()
    board.set_chip("A1")

    print(board.board)
    board.check_board_is_all_completed()
