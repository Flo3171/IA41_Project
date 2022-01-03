import PathSolver


class IA:

    def __init__(self):
        self._path = []

    def solve(self, board):
        ps = PathSolver.PathSolver(None, None, board)
        while ps is not None:
            self._path.append(ps.move)
        return self._path
