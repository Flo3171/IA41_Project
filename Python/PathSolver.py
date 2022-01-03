import Map
import copy
import Direction
import Move


class PathSolver:

    def __init__(self, previous_state, next_state, board):
        self._previousState = previous_state                #type: pathsolver
        self._nextState = next_state                        #type: pathsolver
        self._directions = ['up', 'down', 'left', 'right']
        self._defaultBoard = copy.deepcopy(board)           #type board
        self._currentBoard = copy.deepcopy(board)           #type board
        self._testBoard = copy.deepcopy(board)              #type board
        self._robots = copy.deepcopy(board.robots)          #type liste de robots
        self._playerBot = board.target_robot                #type robot
        self._move = Move.Move(self._playerBot, None)       #type move



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

    def move(self):
        return self._move

    #check si un obstacle est sur la route, avec i et j les coordonnées et i_move et j_move 0,1 ou -1 pour checker la case d'après
    def check_obstacle(self, direction, i, j, i_move, j_move):
        if (self._defaultBoard.case(i + i_move, j + j_move).has_wall_in_dir(direction)) or self._defaultBoard.case(i + i_move, j + j_move).has_bot():
            return True

    #check if a robot is on this case (coord i j) moving in direction d, if it is stopped on the case
    def check_case_to_stop(self, i, j, d):
        if d == 'up':
            if j == 0:      #running into edge of board -> stop
                return True
            else:
                return self.check_obstacle(Direction.Direction.SOUTH, i, j, -1, 0)  #check for other obstacle than edge
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

    #change the choice the solver makes when score of new option is higher than score of current option
    def new_choice(self, test_score, default_score, new_robots, is_robot_better, robot, direction):
        if test_score <= default_score - 1 + is_robot_better:       #if test is better (or same 'cause easier later) than default (is_robot_better is 0 if default is playerbot move, 1 if other robot)
            self._currentBoard = copy.deepcopy(self._testBoard)     #board tested becomes new current board for this state
            self._currentBoard._robots = copy.deepcopy(new_robots)  #board's robots are also moved (probably useless? not sure)
            self._move._robot = robot                               #get robot that made the move to give to ai
            self._move._direction = direction                       #get direction the robot is moving toward to give to ai
            return test_score                                       #return the new score to beat
        else:
            return default_score                                    #else don't change anything and keep same score

    #probably not working ? Using board's bots placement would be better? - Function replaces robot r's position in the new robots list
    def replace_bots(self, new_i, new_j, r):
        new_robots = copy.deepcopy(self._robots)
        for rob in new_robots:
            if rob == r:
                rob._pos = [new_i, new_j]
                return new_robots

    #from change in coordonates, return direction (to later give to ai)
    def get_moved_direction(self, old_x, old_y, new_x, new_y):
        if new_x < old_x:
            return Direction.Direction.NORTH
        elif new_x > old_x:
            return Direction.Direction.SOUTH
        elif new_y < old_y:
            return Direction.Direction.WEST
        else:
            return Direction.Direction.EAST




    #Also probably not working? Idk- Uses map to find where the playerbot must go, according to the map
    def move_current_bot(self, current_map):
        x = self.player_bot().pos().x()
        y = self.player_bot().pos().y()
        for i in range(15):                         #Going through map's matrix to find right case
            for j in range(15):
                if current_map.matrix(i, j) == current_map.mapScore() - 1 and (
                        self._currentBoard.can_go_to_case(i, j, self._playerBot)):  #correct case is mapscore-1 (because one less move) and playerbot can go to it
                    self._currentBoard.case(x, y).remove_bot()                      #remove bot from previous placement
                    self._currentBoard.case(i, j).place_bot(self._playerBot)        #place bot on new placement
                    self._move._direction = self.get_moved_direction(x, y, i, j)    #get direction to give to ai
                    return [i, j]                                                   #return player's position

    #function to keep going unless final state reached
    def keep_searching(self, score):
        if score > 1:               #if mapscore > 1, there are more moves to make, nextstate must be used again
            self._nextState.choose_next_state()
        else:                       #else, mapscore=1 -> nextmove is last one
            x = self._currentBoard.objective().coord().x()
            y = self._currentBoard.objective().coord().y()
            i = self._playerBot.pos.x
            j = self._playerBot.pos.y
            last_board = copy.deepcopy(self._currentBoard)
            last_board.case(i, j).remove_bot()          #manually generate last board
            last_board.case(x, y).place_bot(self._playerBot)
            self._playerBot.pos.x(x)
            self._playerBot.pos.y(y)
            last_move = PathSolver(self._nextState, None, last_board)   #create last state and link to current one
            last_move._move._direction = self.get_moved_direction(i,j,x,y)
            last_move._move._robot = last_move._playerBot
            self._nextState._nextState = last_move

    #"main" function of pathsolver
    def choose_next_state(self):
        default_map = Map.Map(self._playerBot)          #generate map when playerbot is moved
        default_map.generate_map(self._currentBoard)
        new_player_pos = self.move_current_bot(default_map)     #move playerbot on current board and get new positions' coord
        default_score = default_map.map_score           #get mapscore to compare
        is_robot_better = 0                     # 0 means no other bot is moved, 1 means one other bot has moved (on this turn)
        for r in self._robots:
            if r != self._playerBot:            #go through robots that are not playerbot to check other options
                for d in self._directions:
                    i = r.pos().x()
                    j = r.pos().y()
                    new_i = i
                    new_j = j
                    if d == 'up':
                        while not self.check_case_to_stop(new_i, new_j, 'up'):  #find the case where robot stops if moving up
                            new_j -= 1
                        if new_j != j:          #if robot has moved
                            self._testBoard.case(i, j).remove_bot()         #modify the test board to test with new config
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            new_robots = self.replace_bots(new_i, new_j, r)
                            test_map = Map.Map(self._playerBot)             #generate map for new config
                            test_map.generate_map(self._testBoard)
                            test_score = test_map.map_score()
                            default_score = self.new_choice(test_score, default_score, new_robots, is_robot_better, r, Direction.Direction.NORTH) #if option better, change
                            if default_score == test_score: #if score changed, robot has been moved -> no need to compare with -1 -> 1 to compensate
                                is_robot_better = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)  #reset testboard for next test
                    elif d == 'down':       #repeat for each direction
                        while not self.check_case_to_stop(new_i, new_j, 'down'):
                            new_j += 1
                        if new_j != j:
                            self._testBoard.case(i, j).remove_bot()
                            self._testBoard.case(new_i, new_j).place_bot(r)
                            new_robots = self.replace_bots(new_i, new_j, r)
                            test_map = Map.Map(self._playerBot)
                            test_map.generate_map(self._testBoard)
                            test_score = test_map.map_score()
                            default_score = self.new_choice(test_score, default_score, new_robots, is_robot_better, r, Direction.Direction.SOUTH)
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
                            default_score = self.new_choice(test_score, default_score, new_robots, is_robot_better, r, Direction.Direction.WEST)
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
                            default_score = self.new_choice(test_score, default_score, new_robots, is_robot_better, r, Direction.Direction.WEST)
                            if default_score == test_score:
                                is_robot_better = 1
                            self._testBoard = copy.deepcopy(self._defaultBoard)

        i, j = new_player_pos
        if self._currentBoard.cases(i, j).bot() == self._playerBot:
            self._currentBoard._robots = self.replace_bots(i, j, self._playerBot) #if playerbot move is best option, move now

        next_move = PathSolver(self, None, self._currentBoard) #generate nextmove
        self._nextState = next_move

        self.keep_searching(default_score) #keep going


