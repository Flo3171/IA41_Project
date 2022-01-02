import Map
import copy


class PathSolver:

    def __init__(self, previousState, nextState, board, playerBot):
        self._previousState = previousState
        self._nextState = nextState
        self._directions = ['up', 'down', 'left', 'right']
        self._defaultBoard = copy.deepcopy(board)
        self._currentBoard = copy.deepcopy(board)
        self._testBoard = copy.deepcopy(board)
        self._robots = copy.deepcopy(board._robots)
        self._playerBot = copy.deepcopy(playerBot)

    def checkCaseToStop(self, i, j, d):
        if d == 'up':
            if j == 0:
                return True
            elif ([0, 1] in self._defaultBoard._cases[i - 1][j]._walls) or self._defaultBoard._cases[i - 1][
                j]._bot != None:
                return True
        elif d == 'down':
            if j == 15:
                return True
            elif ([0, -1] in self._defaultBoard._cases[i + 1][j]._walls) or self._defaultBoard._cases[i + 1][
                j]._bot != None:
                return True
        elif d == 'left':
            if i == 0:
                return True
            elif ([1, 0] in self._defaultBoard._cases[i][j - 1]._walls) or self._defaultBoard._cases[i][
                j - 1]._bot != None:
                return True
        elif d == 'right':
            if i == 15:
                return True
            elif ([-1, 0] in self._defaultBoard._cases[i][j + 1]._walls) or self._defaultBoard._cases[i][
                j + 1]._bot != None:
                return True
        return False

    def newChoice(self, testScore, defaultScore, newRobots, isRobotBetter):
        if testScore <= defaultScore - 1 + isRobotBetter:
            self._currentBoard = copy.deepcopy(self._testBoard)
            self._currentBoard._robots = copy.deepcopy(newRobots)
            return testScore
        else:
            return defaultScore

    def replaceBots(self, new_i, new_j, r):
        newRobots = copy.deepcopy(self._robots)
        for rob in newRobots:
            if rob == r:
                rob._pos = [new_i, new_j]
                return newRobots

    def moveCurrentBot(self, Map):
        x = self.playerBot().pos().x()
        y = self.playerBot().pos().y()
        for i in range(15):
            for j in range(15):
                if Map._matrix[i][j] == Map._mapScore - 1 and (
                        self._currentBoard._cases[i][j] in self._currentBoard._cases[x][y]._destination):
                    self._currentBoard._cases[x][y]._bot = None
                    self._currentBoard._cases[i][j]._bot = self._playerBot
                    return [i, j]

    def chooseNextState(self):
        defaultMap = Map(self._playerBot)
        defaultMap.generateMap(self._currentBoard)
        newPlayerPos = self.moveCurrentBot(defaultMap)
        defaultScore = defaultMap.mapScore()
        isRobotBetter = 0
        for r in self._robots:
            if r != self._playerBot:
                for d in self._directions:
                    i, j = r._pos
                    new_i = i
                    new_j = j
                    if d == 'up':
                        while (self.checkCaseToStop(new_i, new_j, 'up') == False):
                            new_j -= 1
                        if new_j != j:
                            self._testBoard._cases[i][j]._bot = None
                            self._testBoard._cases[new_i][new_j]._bot = r
                            newRobots = self.replaceBots(new_i, new_j, r)
                            testMap = Map(self._playerBot)
                            testMap.generateMap(self._testBoard)
                            testScore = testMap._mapScore
                            defaultScore = self.newChoice(testScore, defaultScore, newRobots, isRobotBetter)
                            if defaultScore == testScore:
                                isRobotBetter=1
                            self._testBoard = copy.deepcopy(self._defaultBoard)
                    elif d == 'down':
                        while (self.checkCaseToStop(new_i, new_j, 'down') == False):
                            new_j += 1
                        if new_j != j:
                            self._testBoard._cases[i][j]._bot = None
                            self._testBoard._cases[new_i][new_j]._bot = r
                            newRobots = self.replaceBots(new_i, new_j, r)
                            testMap = Map(self._playerBot)
                            testMap.generateMap(self._testBoard)
                            testScore = testMap._mapScore
                            defaultScore = self.newChoice(testScore, defaultScore, newRobots, isRobotBetter)
                            if defaultScore == testScore:
                                isRobotBetter=1
                            self._testBoard = copy.deepcopy(self._defaultBoard)
                    elif d == 'left':
                        while (self.checkCaseToStop(new_i, new_j, 'left') == False):
                            new_i -= 1
                        if new_i != i:
                            self._testBoard._cases[i][j]._bot = None
                            self._testBoard._cases[new_i][new_j]._bot = r
                            newRobots = self.replaceBots(new_i, new_j, r)
                            testMap = Map(self._playerBot)
                            testMap.generateMap(self._testBoard)
                            testScore = testMap._mapScore
                            defaultScore = self.newChoice(testScore, defaultScore, newRobots, isRobotBetter)
                            if defaultScore == testScore:
                                isRobotBetter=1
                            self._testBoard = copy.deepcopy(self._defaultBoard)
                    elif d == 'right':
                        while (self.checkCaseToStop(new_i, new_j, 'right') == False):
                            new_i += 1
                        if new_i != i:
                            self._testBoard._cases[i][j]._bot = None
                            self._testBoard._cases[new_i][new_j]._bot = r
                            newRobots = self.replaceBots(new_i, new_j, r)
                            testMap = Map(self._playerBot)
                            testMap.generateMap(self._testBoard)
                            testScore = testMap._mapScore
                            defaultScore = self.newChoice(testScore, defaultScore, newRobots, isRobotBetter)
                            if defaultScore == testScore:
                                isRobotBetter=1
                            self._testBoard = copy.deepcopy(self._defaultBoard)

        i, j = newPlayerPos
        if self._currentBoard._cases[i][j]._bot == self._playerBot:
            self._currentBoard._robots = self.replaceBots(i, j, self._playerBot)

        nextMove = PathSolver(self, None, self._currentBoard, self._playerBot)
        self._nextState = nextMove

        if defaultScore > 1:
            self._nextState.chooseNextState()
        else:
            x = self._currentBoard.destination().coord().x()
            y = self._currentBoard.destination().coord().y()
            i = self._playerBot.pos().x()
            j = self._playerBot.pos().y()
            lastBoard = copy.deepcopy(self._currentBoard)
            lastBoard._cases[i][j]._bot = None
            lastBoard._cases[x][y]._bot = self._playerBot
            self._playerBot._pos._x = x
            self._playerBot._pos._y = y
            lastMove = PathSolver(self._nextState, None, lastBoard, self._playerBot)
            self._nextState._nextState = lastMove
