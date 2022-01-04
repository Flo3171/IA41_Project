import PathSolver
import CostMap
import Move
import Direction

class AI:

    def __init__(self,  board):
        self._board = board
        self._solution = []

    @property
    def board(self):
        return self._board

    @property
    def solution(self):
        return self._solution

    def solve(self):
        self._solution.append(Move.Move("Yellow", Direction.Direction.NORTH))
        self._solution.append(Move.Move("Yellow", Direction.Direction.EAST))
        self._solution.append(Move.Move("Yellow", Direction.Direction.SOUTH))


    def find_next_move(self):
        cost_map = CostMap.CostMap(self.board)
        cost_map.update_cost_map()
        if cost_map.cost >= 0 :
            print("solution find in "  + cost_map.cost)




