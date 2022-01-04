import PathSolver
import CostMap
import Move
import Direction


class AI:

    def __init__(self, board):
        self._board = board
        self._solution = []
        self._continue_search = True

    @property
    def board(self):
        return self._board

    @property
    def solution(self):
        return self._solution

    @property
    def continue_search(self):
        return self._continue_search

    def stop_search(self):
        self._continue_search = False

    def is_solution_find(self):
        return self.board.target_robot.pos.x == self.board.objective.coord.x and self.board.target_robot.pos.y == self.board.objective.coord.y

    def solve(self):
        cost_map = CostMap.CostMap(self.board)
        cost_map.update_cost_map()
        if cost_map.cost >= 0:
            return cost_map.get_next_move()
        else:
            for r in self.board.robots:
                for d in Direction.get_ordinal_direction_list():
                    print("ok")

    def find_next_move(self):

        cost_map = CostMap.CostMap(self.board)
        cost_map.update_cost_map()
        return cost_map.get_next_move()
