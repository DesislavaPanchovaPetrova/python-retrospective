

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
    KEYS = ["A3", "B3", "C3", "A2", "B2", "C2", "A1", "B1", "C1"]
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
        return ('\n' +
                '  -------------\n' +
                '3 | {} | {} | {} |\n' +
                '  -------------\n' +
                '2 | {} | {} | {} |\n' +
                '  -------------\n' +
                '1 | {} | {} | {} |\n' +
                '  -------------\n' +
                '    A   B   C  \n').format(*[self.board.get(key, " ")
                                              for key in self.KEYS])

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

        self.update_status(self.board)

    def game_status(self):
        return self.status

    def update_status(self, board):
        if self.status == self.GAME_IN_PROGRESS and 4 < len(board):
            if len(self.KEYS) == len(board):
                self.status = self.DRAW
            if self.wins(board, 'X'):
                self.status = self.X_WINS
            elif self.wins(board, 'O'):
                self.status = self.O_WINS

    def wins(self, board, sign):
        board_lines = [[board.get(key) == sign for key in line] for line in self.WIN_LINES]
        victories = ["Wins!" for line in board_lines if line == self.WIN_LINE]
        return any(victories)
