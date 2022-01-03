import PathSolver


class IA:

    def __init__(self):
        self._path = []
        self._color
        self._diretion

    @property
    def color(self):
        return self.color

    @property
    def diretion(self):
        return self._direction

    def solve(self, board):
        ps = PathSolver.PathSolver(None, None, board)
        while ps is not None:
            self._path.append(ps.move)
        return self._path
