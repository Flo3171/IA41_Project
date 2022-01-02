import Board


class Game:
    def __init__(self):
        self._board = Board.Board()
        self._board.generate_board()
