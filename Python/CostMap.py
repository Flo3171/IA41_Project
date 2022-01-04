import Direction
import Coord

class CostMap:

    def __init__(self, board):
        self._matrix = [[-1 for _ in range(16)] for _ in range(16)]  # 16*16 with full -1
        self._board = board
        self._cost = -1
        self._target_robot = self.board.target_robot
        self._objective = self.board.objective

    @property
    def matrix(self):
        return self._matrix

    def matrix_index(self, i, j):
        if 0 <= i < 16 and 0 <= j < 16:
            return self._matrix[i][j]
        else:
            return -2

    def matrix_coord(self, coord):
        return self.matrix_index(coord.x, coord.y)

    @property
    def board(self):
        return self._board

    @property
    def cost(self):
        return self._cost

    @property
    def target_robot(self):
        return self._target_robot

    @property
    def objective(self):
        return self._objective

    def __str__(self):
        value = self._cost.__str__() + "\n     "
        for i in range(16):
            if 0 <= i <= 9:
                value += " "
            value += i.__str__() + " "
        value += "\n\n"
        for j in range(16):
            if 0 <= j <= 9:
                value += " "
            value += j.__str__() + "   "

            for i in range(16):
                if 0 <= self._matrix[i][j] <= 9:
                    value += " "
                value += self._matrix[i][j].__str__() + " "
            value += "\n"
        return value

    def update_cost(self, coord, cost):
        if coord.is_in_map():
            current_cost = self.matrix_coord(coord)
            if 0 > current_cost or current_cost > cost:
                self._matrix[coord.x][coord.y] = cost
                return True
            else:
                return False

    def is_robot_reach(self):
        if self.matrix_coord(self.target_robot.pos) >= 0:
            return True
        else:
            return False

    def update_cost_map(self):
        self.update_cost(self.objective.coord, 0)
        self._cost = self.next_state(0, self.objective.coord)

    def next_state(self, cost, coord_starting):
        print(self)
        if self.is_robot_reach():
            self._cost = self.matrix_coord(self.target_robot.pos)

        elif self.board.case_coord(coord_starting).has_walls():
            for direction in Direction.get_ordinal_direction_list():
                if self.board.case_coord(coord_starting).has_walls_in_dir(direction):
                    opposite_direction = Direction.get_opposite(direction)
                    next_coord = coord_starting
                    while not self.board.is_obstacle(coord_starting, opposite_direction):
                        next_coord = next_coord.add_direction(opposite_direction)
                        if self.update_cost(next_coord, cost + 1):
                            self.next_state(cost + 1, next_coord)


