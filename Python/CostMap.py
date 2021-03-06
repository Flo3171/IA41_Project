import Direction
import Coord
import Move


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
        self.next_state(0, self.objective.coord)

    def is_target_robot_coord(self, coord):
        return coord.is_in_map() \
               and self.board.case_coord(coord).has_bot() \
               and self.board.case_coord(coord).bot.pos.x == self.target_robot.pos.x \
               and self.board.case_coord(coord).bot.pos.y == self.target_robot.pos.y

    def get_next_move(self):
        if self.cost >= 0:
            for d in Direction.get_ordinal_direction_list():
                destination = self.board.case_coord(self.target_robot.pos).destination(d)
                if self.matrix_coord(self.target_robot.pos) - 1 == self.matrix_coord(destination.case.coord):
                    return Move.Move(self.target_robot.color, d)

        else:
            return None



    def next_state(self, cost, coord_starting):

        #print(self)
        if self.is_robot_reach():
            self._cost = self.matrix_coord(self.target_robot.pos)

        else:
            next_cases = []
            for direction in Direction.get_ordinal_direction_list():
                if self.board.case_coord(coord_starting).has_walls_in_dir(direction) or self.board.has_bot_in_dir(coord_starting, direction):
                    opposite_direction = Direction.get_opposite(direction)
                    next_coord = coord_starting
                    while (not self.board.is_obstacle(next_coord, opposite_direction)) or self.is_target_robot_coord(next_coord.add_direction(opposite_direction)):
                        next_coord = next_coord.add_direction(opposite_direction)
                        if self.update_cost(next_coord, cost + 1):
                            next_cases.append(next_coord)

                for coord in next_cases:
                    self.next_state(cost + 1, coord)
