

class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard(object):
    ROWS = "321"
    COLS = "ABC"
    VALUES = ['O', 'X']
    KEYS = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    GAME_IN_PROGRESS = 'Game in progress.'
    DRAW = 'Draw!'
    X_WINS = 'X wins!'
    O_WINS = 'O wins!'
    WIN_LINES = [["A3", "B3", "C3"], ["A2", "B2", "C2"], ["A1", "B1", "C1"],
                 ["A3", "A2", "A1"], ["B3", "B2", "B1"], ["C3", "C2", "C1"],
                 ["A3", "B2", "C1"], ["A1", "B2", "C3"]]
    WIN_LINE = [True, True, True]

    def __init__(self):
        self.board = dict()
        self.turn = None
        self.status = self.GAME_IN_PROGRESS

    def __str__(self):
        board_str = ""
        for row in self.ROWS:
            board_str += "\n  -------------\n"
            board_str += str(row)+" |"
            for col in self.COLS:
                key = col+str(row)
                board_str += " "+self.board.get(key, " ")+" |"
        board_str += "\n  -------------\n    A   B   C  \n"
        return board_str

    def __setitem__(self, key, value):
        if value not in self.VALUES:
            raise InvalidValue("Use 'X' or 'O' for value.")

        if key not in self.KEYS:
            raise InvalidKey("Wrong position!")

        if key in self.board:
            raise InvalidMove("This position is taken!")

        if self.turn and self.turn == value:
            raise NotYourTurn("Not your turn!")
        else:
            self.turn = value

        self.board[key] = value

        if self.status == self.GAME_IN_PROGRESS and 4 < len(self.board):
            if 9 == len(self.board):
                self.status = self.DRAW
            if self.wins(self.board, 'X'):
                self.status = self.X_WINS
            if self.wins(self.board, 'O'):
                self.status = self.O_WINS

    def game_status(self):
        return self.status

    def wins(self, board, sign):
        board_lines = [[board.get(key) == sign for key in line] for line in self.WIN_LINES]
        victories = ["Wins!" for line in board_lines if line == self.WIN_LINE]
        return any(victories)
