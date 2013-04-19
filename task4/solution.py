from functools import reduce


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard(object):
    def __init__(self):
        self.board = dict()
        self.turn = None
        self.status = "Game in progress."

    def __str__(self):
        board_str = ""
        for row in [3, 2, 1]:
            board_str += "\n  -------------\n"
            board_str += str(row)+" |"
            for col in "ABC":
                key = col+str(row)
                board_str += " "+self.board.get(key, " ")+" |"
        board_str += "\n  -------------\n    A   B   C  \n"
        return board_str

    def __setitem__(self, key, value):
        if value != 'O' and value != 'X':
            raise InvalidValue("Use 'X' or 'O' for value.")

        if key not in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            raise InvalidKey("Wrong position!")

        if key in self.board:
            raise InvalidMove("This position is taken!")

        if self.turn is not None and self.turn == value:
            raise NotYourTurn("Not your turn!")
        else:
            self.turn = value

        self.board[key] = value

        if self.status == "Game in progress." and 4 < len(self.board):
            if 9 == len(self.board):
                self.status = 'Draw!'
            if self.wins(self.board, 'X'):
                self.status = 'X wins!'
            if self.wins(self.board, 'O'):
                self.status = 'O wins!'

    def game_status(self):
        return self.status

    def wins(self, board, sign):
        winLines = [["A3", "B3", "C3"], ["A2", "B2", "C2"], ["A1", "B1", "C1"],
                    ["A3", "A2", "A1"], ["B3", "B2", "B1"], ["C3", "C2", "C1"],
                    ["A3", "B2", "C1"], ["A1", "B2", "C3"]]
        values = [[board.get(l) == sign for l in line] for line in winLines]
        wins = [reduce(lambda x, y: x and y, value) for value in values]
        winer = reduce(lambda x, y: x or y, wins)
        return winer
