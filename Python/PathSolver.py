import Map
import copy
import Direction


class PathSolver:

    def __init__(self, previous_state, next_state, board):
        self._previousState = previous_state
        self._nextState = next_state
        self._directions = ['up', 'down', 'left', 'right']
        self._defaultBoard = copy.deepcopy(board)
        self._currentBoard = copy.deepcopy(board)
        self._testBoard = copy.deepcopy(board)
        self._robots = copy.deepcopy(board.robots)
        self._playerBot = board.target_robot



    @property
    def robots(self):
        return self._robots

    def robot(self, i):
        return self._robots[i]

    @property
    def player_bot(self):
        return self._playerBot

    @property
    def board(self):
        return self._currentBoard

    def check_obstacle(self, direction, i, j, i_move, j_move):
        if (self._defaultBoard.case(i + i_move, j + j_move).has_wall_in_dir(direction)) or self._defaultBoard.case(i + i_move, j + j_move).has_bot():
            return True

    def check_case_to_stop(self, i, j, d):
        if d == 'up':
            if j == 0:
                return True
            else:
                return self.check_obstacle(Direction.Direction.SOUTH, i, j, -1, 0)
        elif d == 'down':
            if j == 15:
                return True
            else:
                return self.check_obstacle(Direction.Direction.NORTH, i, j, 1, 0)
        elif d == 'left':
            if i == 0:
                return True
            else:
                return self.check_obstacle(Direction.Direction.EAST, i, j, 0, -1)
        elif d == 'right':
            if i == 15:
                return True
            else:
                return self.check_obstacle(Direction.Direction.WEST, i, j, 0, 1)
        return False

    def new_choice(self, test_score, default_score, new_robots, is_robot_better):
        if test_score <= default_score - 1 + is_robot_better:
            self._currentBoard = copy.deepcopy(self._testBoard)
            self._currentBoard._robots = copy.deepcopy(new_robots)
            return test_score
        else:
            return default_score

    def replace_bots(self, new_i, new_j, r):
        new_robots = copy.deepcopy(self._robots)
        for rob in new_robots:
            if rob == r:
                rob._pos = [new_i, new_j]
                return new_robots

    def move_current_bot(self, current_map):
        x = self.player_bot().pos().x()
        y = self.player_bot().pos().y()
        for i in range(15):
            for j in range(15):
                if current_map.matrix(i, j) == current_map.mapScore() - 1 and (
                        self._currentBoard.case(i, j) in self._currentBoard.case(x, y).destination()):
                    self._currentBoard.case(x, y).remove_bot()
                    self._currentBoard.case(i, j).place_bot(self._playerBot)
                    return [i, j]

    def keep_searching(self, score):
        if score > 1:
            self._nextState.choose_next_state()
        else:
            x = self._currentBoard.destination().coord().x()
            y = self._currentBoard.destination().coord().y()
            i = self._playerBot.pos.x
            j = self._playerBot.pos.y
            last_board = copy.deepcopy(self._currentBoard)
            last_board.case(i, j).remove_bot()
            last_board.case(x, y).place_bot(self._playerBot)
            self._playerBot.pos.x(x)
            self._playerBot.pos.y(y)
            last_move = PathSolver(self._nextState, None, last_board)
            self._nextState._nextState = last_move

    def choose_next_state(self):
        default_map = Map.Map(self._playerBot)
        default_map.generate_map(self._currentBoard)
        new_player_pos = self.move_current_bot(default_map)
        default_score = default_map.map_score
        is_robot_better = 0
        for r in self._robots:
            if r != self._playerBot:
                for d in self._directions:
                    i = r.pos().x()
                    j = r.pos().y()
                    new_i = i
                    new_j = j
                    if d == 'up':
                        while not self.check_case_to_stop(new_i, new_j, 'up'):
                            new_j -= 1
                        if new_j != j:
                            self._testBoard.case(i, j).remove_bot()
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            new_robots = self.replace_bots(new_i, new_j, r)
                            test_map = Map.Map(self._playerBot)
                            test_map.generate_map(self._testBoard)
                            test_score = test_map.map_score()
                            default_score = self.new_choice(test_score, default_score, new_robots, is_robot_better)
                            if default_score == test_score:
                                is_robot_better = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)
                    elif d == 'down':
                        while not self.check_case_to_stop(new_i, new_j, 'down'):
                            new_j += 1
                        if new_j != j:
                            self._testBoard.case(i, j).remove_bot()
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            new_robots = self.replace_bots(new_i, new_j, r)
                            test_map = Map.Map(self._playerBot)
                            test_map.generate_map(self._testBoard)
                            test_score = test_map.map_score()
                            default_score = self.new_choice(test_score, default_score, new_robots, is_robot_better)
                            if default_score == test_score:
                                is_robot_better = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)
                    elif d == 'left':
                        while not self.check_case_to_stop(new_i, new_j, 'left'):
                            new_i -= 1
                        if new_i != i:
                            self._testBoard.case(i, j).remove_bot()
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            new_robots = self.replace_bots(new_i, new_j, r)
                            test_map = Map.Map(self._playerBot)
                            test_map.generate_map(self._testBoard)
                            test_score = test_map.map_score()
                            default_score = self.new_choice(test_score, default_score, new_robots, is_robot_better)
                            if default_score == test_score:
                                is_robot_better = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)
                    elif d == 'right':
                        while not self.check_case_to_stop(new_i, new_j, 'right'):
                            new_i += 1
                        if new_i != i:
                            self._testBoard.case(i, j).remove_bot()
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            new_robots = self.replace_bots(new_i, new_j, r)
                            test_map = Map.Map(self._playerBot)
                            test_map.generate_map(self._testBoard)
                            test_score = test_map.map_score()
                            default_score = self.new_choice(test_score, default_score, new_robots, is_robot_better)
                            if default_score == test_score:
                                is_robot_better = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)

        i, j = new_player_pos
        if self._currentBoard.cases(i, j).bot() == self._playerBot:
            self._currentBoard._robots = self.replace_bots(i, j, self._playerBot)

        next_move = PathSolver(self, None, self._currentBoard)
        self._nextState = next_move

        self.keep_searching(default_score)


