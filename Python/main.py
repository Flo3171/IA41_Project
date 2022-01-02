import Board
import PathSolver

b = Board.Board()
b.generate_board()

path = PathSolver.PathSolver(None, None, b)
