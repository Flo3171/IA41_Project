import PathSolver
import CostMap
import Move
import Direction
import Coord


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
            self.solution.append(cost_map.get_next_move())
        else:
            for color in ["Blue", "Green", "Red", "Yellow"]:
                for d in Direction.get_ordinal_direction_list():
                    robot = self.board.robot(color)
                    initial_pos = Coord(robot.pos.x, robot.pos.y)
                    move = Move.Move(color, d)
                    self.board.move_bot_move(move)
                    new_cost_map = CostMap.CostMap(self.board)
                    new_cost_map.update_cost_map()
                    if cost_map.cost >= 0:
                        self.solution.append(move)
                    self.board.move_bot(color, initial_pos)


