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
        self._robots = copy.deepcopy(board.robots())

        for i in range(4):
            if self.robots[i]().color() == board.objective.game_object[0]:
                self._playerBot = self.robots[i]()

    @property
    def robots(self):
        return self._robots

    @property
    def player_bot(self):
        return self._playerBot

    def check_case_to_stop(self, i, j, d):
        if d == 'up':
            if j == 0:
                return True
            elif (
                    self._defaultBoard.case(i - 1, j).has_wall_in_dir(
                        Direction.Direction.NORTH)) or self._defaultBoard.case(
                    i - 1, j).has_bot():
                return True
        elif d == 'down':
            if j == 15:
                return True
            elif (
                    self._defaultBoard.cases(i + 1, j).has_wall_in_dir(
                        Direction.Direction.NORTH)) or self._defaultBoard.case(
                    i + 1, j).has_bot():
                return True
        elif d == 'left':
            if i == 0:
                return True
            elif (
                    self._defaultBoard.cases(i, j - 1).has_wall_in_dir(
                        Direction.Direction.EAST)) or self._defaultBoard.case(i,
                                                                              j - 1).has_bot():
                return True
        elif d == 'right':
            if i == 15:
                return True
            elif ([-1, 0] in self._defaultBoard.case(i, j + 1).has_wall_in_dir(
                    Direction.Direction.WEST)) or self._defaultBoard.case(i, j + 1).has_bot():
                return True
        return False

    def new_choice(self, test_score, default_score, new_robots, is_robot_better):
        if test_score <= default_score - 1 + is_robot_better:
            self._currentBoard = copy.deepcopy(self._testBoard)
            self._currentBoard._robots = copy.deepcopy(new_robots)
            return test_score
        else:
            return default_score

    def replace_bots(self, new_i, new_j, r):
        newRobots = copy.deepcopy(self._robots)
        for rob in newRobots:
            if rob == r:
                rob._pos = [new_i, new_j]
                return newRobots

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

    def choose_next_state(self):
        defaultMap = Map.Map(self._playerBot)
        defaultMap.generate_map(self._currentBoard)
        newPlayerPos = self.move_current_bot(defaultMap)
        defaultScore = defaultMap.map_score()
        isRobotBetter = 0
        for r in self._robots:
            if r != self._playerBot:
                for d in self._directions:
                    i = r.pos().x()
                    j = r.pos().y()
                    new_i = i
                    new_j = j
                    if d == 'up':
                        while self.check_case_to_stop(new_i, new_j, 'up') is False:
                            new_j -= 1
                        if new_j != j:
                            self._testBoard.case(i, j).remove_bot()
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            newRobots = self.replace_bots(new_i, new_j, r)
                            testMap = Map.Map(self._playerBot)
                            testMap.generate_map(self._testBoard)
                            testScore = testMap.map_score()
                            defaultScore = self.new_choice(testScore, defaultScore, newRobots, isRobotBetter)
                            if defaultScore == testScore:
                                isRobotBetter = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)
                    elif d == 'down':
                        while not self.check_case_to_stop(new_i, new_j, 'down'):
                            new_j += 1
                        if new_j != j:
                            self._testBoard.case(i, j).remove_bot()
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            newRobots = self.replace_bots(new_i, new_j, r)
                            testMap = Map.Map(self._playerBot)
                            testMap.generate_map(self._testBoard)
                            testScore = testMap.map_score()
                            defaultScore = self.new_choice(testScore, defaultScore, newRobots, isRobotBetter)
                            if defaultScore == testScore:
                                isRobotBetter = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)
                    elif d == 'left':
                        while not self.check_case_to_stop(new_i, new_j, 'left'):
                            new_i -= 1
                        if new_i != i:
                            self._testBoard.case(i, j).remove_bot()
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            newRobots = self.replace_bots(new_i, new_j, r)
                            testMap = Map.Map(self._playerBot)
                            testMap.generate_map(self._testBoard)
                            testScore = testMap.map_score()
                            defaultScore = self.new_choice(testScore, defaultScore, newRobots, isRobotBetter)
                            if defaultScore == testScore:
                                isRobotBetter = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)
                    elif d == 'right':
                        while not self.check_case_to_stop(new_i, new_j, 'right'):
                            new_i += 1
                        if new_i != i:
                            self._testBoard.case(i, j).remove_bot()
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            newRobots = self.replace_bots(new_i, new_j, r)
                            testMap = Map.Map(self._playerBot)
                            testMap.generate_map(self._testBoard)
                            testScore = testMap.map_score()
                            defaultScore = self.new_choice(testScore, defaultScore, newRobots, isRobotBetter)
                            if defaultScore == testScore:
                                isRobotBetter = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)

        i, j = newPlayerPos
        if self._currentBoard.cases(i, j).bot() == self._playerBot:
            self._currentBoard._robots = self.replace_bots(i, j, self._playerBot)

        nextMove = PathSolver(self, None, self._currentBoard)
        self._nextState = nextMove

        if defaultScore > 1:
            self._nextState.choose_next_state()
        else:
            x = self._currentBoard.destination().coord().x()
            y = self._currentBoard.destination().coord().y()
            i = self._playerBot.pos().x()
            j = self._playerBot.pos().y()
            lastBoard = copy.deepcopy(self._currentBoard)
            lastBoard.case(i, j).remove_bot()
            lastBoard.case(x, y).place_bot(self._playerBot)
            self._playerBot.pos().x(x)
            self._playerBot.pos().y(y)
            lastMove = PathSolver(self._nextState, None, lastBoard)
            self._nextState._nextState = lastMove
