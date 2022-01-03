import numpy as np


class Map:

    def __init__(self, player_bot):
        self._matrix = []
        self._matrix = [[0 for _ in range(16)] for _ in range(16)]  # matrix full of 0
        self._directions = [np.array([0, 1]), np.array([0, -1]), np.array([1, 0]),
                            np.array([-1, 0])]  # down up right left
        self._playerBot = player_bot  # Robot that must reach destination
        self._mapScore = 0  # Less expensive path

    def matrix(self, i, j):
        return self._matrix[i][j]

    @property
    def map_score(self):
        return self._mapScore

    def add_value(self, i, j, move_cost):
        if self._matrix[i][j] == 0:
            self._matrix[i][j] = move_cost

    def add_to_map(self, i, j, move_cost, board):
        for d in self._directions:
            for k in range(2, 16):
                new_d_plus = d * k + np.array([i, j])
                new_d = d * (k - 1) + np.array([i, j])
                new_i_plus, new_j_plus = list(new_d_plus)
                new_i, new_j = list(new_d)
                nextTo_i = 0
                nextTo_j = 0

                if d[0] == 0:
                    nextTo_i = 1
                else:
                    nextTo_j = 1
                if 0 <= new_i <= 15 and 0 <= new_j <= 15:
                    if 0 <= new_i_plus <= 15 and 0 <= new_j_plus <= 15:
                        if board.case(new_i, new_j).has_bot():
                            if board.case(new_i, new_j).bot == self._playerBot:
                                self.add_value(new_i, new_j, move_cost)
                                return move_cost
                        elif (not board.case(new_i, new_j).has_walls()) and (
                                not board.case(new_i, new_j).has_walls_in_dir(d)):
                            self.add_value(new_i, new_j, move_cost)
                            break
                        elif (board.case(new_i + nextTo_i, new_j + nextTo_j).bot() is not None) or (
                                board.case(new_i - nextTo_i, new_j - nextTo_j).bot() is not None):
                            self.add_value(new_i, new_j, move_cost)
                            break
                        elif (not board.case(new_i, new_j).has_walls_in_dir(d)) or (
                                board.case(new_i_plus, new_j_plus).bot() is not None):
                            break
                    elif new_i == 0 or new_i == 15 or new_j == 0 or new_j == 15:
                        if board.case(new_i, new_j).has_bot():
                            if board.case(new_i, new_j).bot == self._playerBot:
                                self.add_value(new_i, new_j, move_cost)
                                return move_cost
                        elif (board.case(new_i, new_j).has_walls_in_dir(d)) and (
                                board.case(new_i, new_j).has_bot()):
                            self.add_value(new_i, new_j, move_cost)
                            break
                        elif (board.case(new_i + nextTo_i, new_j + nextTo_j).bot() is not None) or (
                                board.case(new_i - nextTo_i, new_j - nextTo_j).bot() is not None):
                            self.add_value(new_i, new_j, move_cost)
                            break
        return 0

    def generate_map(self, board):
        foundRobot = False
        moveCost = 1
        x = board.objective.coord.x
        y = board.objective.coord.y
        self.add_value(x, y, 50)  # Value assigned to destination, that shouldn't be reached otherwise
        while not foundRobot:
            for i in range(15):
                for j in range(15):
                    if (self._matrix[i][j] == moveCost - 1 and moveCost != 1) or (self._matrix == 50 and moveCost == 1):
                        a = self.add_to_map(i, j, moveCost, board)
                        if a != 0:
                            foundRobot = True
                            self._mapScore = a
            moveCost += 1
