import Case
import Coord
import Wall
import Direction
import GameObject
import Robot
import Destination
import random
import Objective
import PathSolver


class Board:

    def __init__(self):
        # init the board
        self._cases = [[Case.Case(Coord.Coord(j, i)) for i in range(16)] for j in range(16)]
        self._robots = []
        self._objective = None
        self._target_robot = None

    @property
    def cases(self):
        return self._cases

    @property
    def robots(self):
        return self._robots

    def robot(self, objective_color):
        for i in range(4):
            if self._robots[i].color == objective_color:
                return self._robots[i]

    @property
    def objective(self):
        return self._objective

    def case(self, i, j):
        if 0 <= i < 16 and 0 <= j < 16:
            return self._cases[i][j]
        else:
            return Case.Case(Coord.Coord(i, j))

    def case_coord(self, coord):
        return self.case(coord.x, coord.y)

    @property
    def target_robot(self):
        return self._target_robot

    def choose_objective(self, game_object):
        # set the objective to reach with the robot
        if game_object is None:
            game_object = random.choice(list(GameObject.GameObject))
        while game_object == GameObject.GameObject.VORTEX:
            game_object = random.choice(list(GameObject.GameObject))
        self._objective = Objective.Objective(self.find_game_object(game_object), game_object)

        self.update_target_robot()

    def update_target_robot(self):
        if self.objective.game_object.value == 0:
            objective_color = None
        elif self.objective.game_object.value % 4 == 1:
            objective_color = "Blue"
        elif self.objective.game_object.value % 4 == 2:
            objective_color = "Red"
        elif self.objective.game_object.value % 4 == 3:
            objective_color = "Green"
        else:
            objective_color = "Yellow"

        for i in range(4):
            if self._robots[i].color == objective_color:
                self._target_robot = self._robots[i]

    def move_bot_move(self, move):
        cord = Board.case(self, Board.robot(self, move.robot_color).pos.x,
                               Board.robot(self, move.robot_color).pos.y).destination(move.direction).case.coord
        Board.move_bot(self, move.robot_color, cord)

    def generate_board(self):
        self.generate_default_wall()
        self.generate_template(False)
        self.generate_robot()
        self.update_destination()

    def generate_default_wall(self):

        for j in range(16):
            # put the wall around the map
            self._cases[j][0].add_wall(Wall.Wall(Direction.Direction.NORTH))
            self._cases[0][j].add_wall(Wall.Wall(Direction.Direction.WEST))
            self._cases[j][15].add_wall(Wall.Wall(Direction.Direction.SOUTH))
            self._cases[15][j].add_wall(Wall.Wall(Direction.Direction.EAST))

            for i in range(16):

                # put the wall around the central block
                if i == 7 or i == 8:
                    if j == 6:
                        self._cases[i][6].add_wall(Wall.Wall(Direction.Direction.SOUTH))
                    elif j == 9:
                        self._cases[i][9].add_wall(Wall.Wall(Direction.Direction.NORTH))
                elif j == 7 or j == 8:
                    if i == 6:
                        self._cases[6][j].add_wall(Wall.Wall(Direction.Direction.EAST))
                    elif i == 9:
                        self._cases[9][j].add_wall(Wall.Wall(Direction.Direction.WEST))

    def generate_template(self, fix):

        available_quarter = [True, True, True, True]
        # put one template on each quarter map
        for i in range(4):

            if fix:
                template = i
            else:
                template = random.randint(0, 15)
                while not available_quarter[template % 4]:
                    template = random.randint(0, 15)

            available_quarter[template % 4] = False

            if template == 0:
                # template number 0
                self.put_wall(Coord.Coord(1, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(2, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 5), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 6), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(4, 1), i, GameObject.GameObject.RED_BALL,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(1, 2), i, GameObject.GameObject.GREEN_BEACON,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(6, 3), i, GameObject.GameObject.YELLOW_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(4, 6), i, GameObject.GameObject.BLUE_RING,
                                Direction.Direction.SOUTH_WEST)

            elif template == 1:
                # template number 1
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 3), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 4), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(5, 1), i, GameObject.GameObject.GREEN_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(1, 2), i, GameObject.GameObject.RED_RING,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(6, 4), i, GameObject.GameObject.YELLOW_BALL,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(2, 6), i, GameObject.GameObject.BLUE_BEACON,
                                Direction.Direction.NORTH_EAST)

            elif template == 2:
                # template number 2
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 4), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 5), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(5, 2), i, GameObject.GameObject.BLUE_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(2, 4), i, GameObject.GameObject.GREEN_BALL,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(7, 5), i, GameObject.GameObject.RED_BEACON,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(1, 6), i, GameObject.GameObject.YELLOW_RING,
                                Direction.Direction.NORTH_WEST)

            elif template == 3:
                # template number 3
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 6), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 7), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(6, 1), i, GameObject.GameObject.BLUE_BALL,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(1, 3), i, GameObject.GameObject.YELLOW_BEACON,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(5, 4), i, GameObject.GameObject.GREEN_RING,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(2, 5), i, GameObject.GameObject.RED_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(7, 5), i, GameObject.GameObject.VORTEX, Direction.Direction.SOUTH_EAST)

            elif template == 4:
                # template number 4
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 5), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 6), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(6, 1), i, GameObject.GameObject.YELLOW_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(1, 2), i, GameObject.GameObject.GREEN_BEACON,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(6, 5), i, GameObject.GameObject.BLUE_RING,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(3, 6), i, GameObject.GameObject.RED_BALL,
                                Direction.Direction.SOUTH_WEST)

            elif template == 5:
                # template number 5
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 4), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 5), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(2, 1), i, GameObject.GameObject.YELLOW_BALL,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(6, 3), i, GameObject.GameObject.BLUE_BEACON,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(4, 5), i, GameObject.GameObject.RED_RING,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(1, 6), i, GameObject.GameObject.GREEN_COIN,
                                Direction.Direction.SOUTH_WEST)

            elif template == 6:
                # template number 6
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 5), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 6), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(1, 1), i, GameObject.GameObject.RED_BEACON,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(6, 2), i, GameObject.GameObject.GREEN_BALL,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(2, 4), i, GameObject.GameObject.BLUE_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(7, 5), i, GameObject.GameObject.YELLOW_RING,
                                Direction.Direction.NORTH_WEST)

            elif template == 7:
                # template number 7
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 4), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 5), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(2, 1), i, GameObject.GameObject.RED_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(1, 3), i, GameObject.GameObject.GREEN_RING,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(6, 4), i, GameObject.GameObject.YELLOW_BEACON,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(5, 6), i, GameObject.GameObject.BLUE_BALL,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(3, 7), i, GameObject.GameObject.VORTEX, Direction.Direction.SOUTH_EAST)

            elif template == 8:
                # template number 8
                self.put_wall(Coord.Coord(1, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(2, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 6), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 7), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(3, 1), i, GameObject.GameObject.GREEN_BEACON,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(6, 3), i, GameObject.GameObject.YELLOW_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(1, 4), i, GameObject.GameObject.RED_BALL,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(4, 6), i, GameObject.GameObject.BLUE_RING,
                                Direction.Direction.NORTH_EAST)

            elif template == 9:
                # template number 9
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(6, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 3), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 4), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(3, 2), i, GameObject.GameObject.YELLOW_BALL,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(5, 3), i, GameObject.GameObject.BLUE_BEACON,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(2, 4), i, GameObject.GameObject.RED_RING,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(4, 5), i, GameObject.GameObject.GREEN_COIN,
                                Direction.Direction.SOUTH_WEST)

            elif template == 10:
                # template number 10
                self.put_wall(Coord.Coord(1, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(2, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 5), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 6), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(4, 1), i, GameObject.GameObject.GREEN_BALL,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(1, 3), i, GameObject.GameObject.RED_BEACON,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(5, 5), i, GameObject.GameObject.YELLOW_RING,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(3, 6), i, GameObject.GameObject.BLUE_COIN,
                                Direction.Direction.SOUTH_EAST)

            elif template == 11:
                # template number 11
                self.put_wall(Coord.Coord(2, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 3), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 4), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(5, 1), i, GameObject.GameObject.BLUE_BALL,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(3, 4), i, GameObject.GameObject.RED_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(6, 5), i, GameObject.GameObject.GREEN_RING,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(1, 6), i, GameObject.GameObject.YELLOW_BEACON,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(7, 1), i, GameObject.GameObject.VORTEX, Direction.Direction.SOUTH_WEST)

            elif template == 12:
                # template number 12
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(6, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 5), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 6), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(1, 3), i, GameObject.GameObject.RED_BALL,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(6, 4), i, GameObject.GameObject.YELLOW_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(2, 6), i, GameObject.GameObject.GREEN_BEACON,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(3, 6), i, GameObject.GameObject.BLUE_RING,
                                Direction.Direction.SOUTH_WEST)

            elif template == 13:
                # template number 13
                self.put_wall(Coord.Coord(2, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 6), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 7), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(5, 2), i, GameObject.GameObject.GREEN_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(6, 2), i, GameObject.GameObject.YELLOW_BALL,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(1, 5), i, GameObject.GameObject.RED_RING,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(4, 7), i, GameObject.GameObject.BLUE_BEACON,
                                Direction.Direction.NORTH_EAST)

            elif template == 14:
                # template number 14
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 2), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 3), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(6, 2), i, GameObject.GameObject.BLUE_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(2, 4), i, GameObject.GameObject.GREEN_BALL,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(3, 4), i, GameObject.GameObject.RED_BEACON,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(5, 6), i, GameObject.GameObject.YELLOW_RING,
                                Direction.Direction.NORTH_WEST)

            elif template == 15:
                # template number 15
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 6), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 7), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(6, 2), i, GameObject.GameObject.YELLOW_BEACON,
                                Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(2, 3), i, GameObject.GameObject.BLUE_BALL,
                                Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(3, 3), i, GameObject.GameObject.GREEN_RING,
                                Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(1, 5), i, GameObject.GameObject.RED_COIN,
                                Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(5, 7), i, GameObject.GameObject.VORTEX, Direction.Direction.SOUTH_EAST)

    def generate_robot(self):
        # create and set the position of the robot
        colors = ["Blue", "Green", "Red", "Yellow"]
        for i in range(4):
            coord_x = random.randint(0, 15)
            coord_y = random.randint(0, 15)
            board_case = self._cases[coord_x][coord_y]
            while (((6 < coord_x < 9) and (
                    6 < coord_y < 9)) or board_case.has_game_object() or board_case.has_bot()):
                coord_x = random.randint(0, 15)
                coord_y = random.randint(0, 15)
                board_case = self._cases[coord_x][coord_y]
            robot = Robot.Robot(colors[i], Coord.Coord(coord_x, coord_y))
            self._robots.append(robot)
            board_case.place_bot(robot)

    def update_destination(self):
        # we store in each case of the plate, the case accessible in 1 move
        for j in range(16):
            for i in range(16):
                if (j < 7 or j > 8) or (i < 7 or i > 8):
                    self.case(i, j).reset_destinations()
                    destinations = self.link_case(i, j)
                    for d in destinations:
                        self._cases[i][j].add_destination(d)

    def has_bot_in_dir(self, coord, direction):
        return self.case(coord.x + Direction.get_x(direction), coord.y + Direction.get_y(direction)).has_bot()

    def is_obstacle(self, coord, direction):
        return not Coord.Coord(coord.x + Direction.get_x(direction),
                               coord.y + Direction.get_y(direction)).is_in_map() or self.case_coord(
            coord).has_walls_in_dir(direction) or self.has_bot_in_dir(
            coord, direction)

        # Methods to compute for each case the cases on which we can go in one move

    def link_case(self, x, y):
        can_go = []

        for direction in Direction.get_ordinal_direction_list():
            actual_x = x
            actual_y = y
            actual_coord = Coord.Coord(actual_x, actual_y)
            # While the actual case has no wall in the direction we follow
            while not self.is_obstacle(actual_coord, direction):
                # If there is no obstacle, we increase the test coordinates, and we loop
                actual_x += Direction.get_x(direction)
                actual_y += Direction.get_y(direction)
                actual_coord = Coord.Coord(actual_x, actual_y)

            # When we exit the loop, we create a new destination with the last test coordinates
            can_go.append(Destination.Destination(direction, self._cases[actual_x][actual_y]))

        return can_go

    def find_game_object(self, game_object):
        for j in range(16):
            for i in range(16):
                if self._cases[i][j].game_object() == game_object:
                    return Coord.Coord(i, j)
        return None

    # Methods to compute for each case the cases on which we can go in one move
    def next_states(self, x, y):
        directions = [
            Direction.Direction.NORTH,
            Direction.Direction.EAST,
            Direction.Direction.SOUTH,
            Direction.Direction.WEST,
        ]
        can_go = []

        for direction in directions:
            actual_x = x
            actual_y = y
            # While the actual case has no wall in the direction we follow
            while not self._cases[actual_x][actual_y].has_walls_in_dir(direction):
                # If the next case has a bot, we stop
                if self._cases[actual_x + Direction.get_x(direction)][actual_y + Direction.get_y(direction)].has_bot:
                    break
                # If there is no obstacle, we increase the test coordinates, and we loop
                actual_x += Direction.get_x(direction)
                actual_y += Direction.get_y(direction)

            # When we exit the loop, we create a new destination with the last test coordinates
            can_go.append(Destination.Destination(direction, self._cases[actual_x][actual_y]))

        return can_go

    def put_wall(self, coord, direction, rotation):
        if 0 <= coord.x < 16 and 0 <= coord.y < 16:
            new_cord = coord.rotate(rotation)
            self._cases[new_cord.x][new_cord.y].add_wall(Wall.Wall(Direction.get_n_adjacent(direction, rotation)))

    def put_object(self, coord, rotation, obj, direction):
        new_cord = coord.rotate(rotation)
        self._cases[new_cord.x][new_cord.y].add_game_object(obj)

        if direction == Direction.Direction.NORTH_EAST:
            self.put_wall(coord, Direction.Direction.NORTH, rotation)
            self.put_wall(Coord.Coord(coord.x, coord.y - 1), Direction.Direction.SOUTH, rotation)

            self.put_wall(coord, Direction.Direction.EAST, rotation)
            self.put_wall(Coord.Coord(coord.x + 1, coord.y), Direction.Direction.WEST, rotation)

        elif direction == Direction.Direction.SOUTH_EAST:
            self.put_wall(Coord.Coord(coord.x, coord.y + 1), Direction.Direction.NORTH, rotation)
            self.put_wall(coord, Direction.Direction.SOUTH, rotation)

            self.put_wall(coord, Direction.Direction.EAST, rotation)
            self.put_wall(Coord.Coord(coord.x + 1, coord.y), Direction.Direction.WEST, rotation)

        elif direction == Direction.Direction.SOUTH_WEST:
            self.put_wall(Coord.Coord(coord.x, coord.y + 1), Direction.Direction.NORTH, rotation)
            self.put_wall(coord, Direction.Direction.SOUTH, rotation)

            self.put_wall(Coord.Coord(coord.x - 1, coord.y), Direction.Direction.EAST, rotation)
            self.put_wall(coord, Direction.Direction.WEST, rotation)

        elif direction == Direction.Direction.NORTH_WEST:
            self.put_wall(coord, Direction.Direction.NORTH, rotation)
            self.put_wall(Coord.Coord(coord.x, coord.y - 1), Direction.Direction.SOUTH, rotation)

            self.put_wall(Coord.Coord(coord.x - 1, coord.y), Direction.Direction.EAST, rotation)
            self.put_wall(coord, Direction.Direction.WEST, rotation)

        return Objective.Objective(new_cord, obj)

    # Method that check in a radius of one around de given coordinates if there is another object
    def is_nearby(self, x, y):
        y_test = y - 1
        for i in range(3):
            x_test = x - 1
            for j in range(3):
                if (
                        self._cases[x_test][y_test].has_game_object()
                        or x_test == 7
                        or x_test == 8
                        or y_test == 7
                        or y_test == 8
                ):
                    return True
                x_test += 1
            y_test += 1
        return False

    # Method to move a bot by giving it color and the new coord
    def move_bot(self, color, coord):
        for i in range(16):
            for j in range(16):
                if self._cases[i][j].has_bot():
                    if self._cases[i][j].bot.color == color:
                        robot = self._cases[i][j].bot
                        self._cases[i][j].bot.move(coord)
                        self._cases[coord.x][coord.y].place_bot(robot)
                        self._cases[i][j].remove_bot()
                        break
            else:
                continue
            break
        self.update_destination()

    def move_bot_direction(self, color, direction):
        cordonnee = Board.case(self, Board.robot(self, color).pos.x,
                               Board.robot(self, color).pos.y).destination(direction).case.coord
        Board.move_bot(self, color, cordonnee)

    # depreciated
    # Method to move a bot after finding a valid place
    def move_valid_bot(self, robot, direction):
        s = PathSolver.PathSolver(None, None, self)
        x = robot.pos().x()
        y = robot.pos().y()
        if direction == Direction.Direction.NORTH:
            for i in range(16):
                if x - i >= 0:
                    if s.check_case_to_stop(x - i, y, 'up'):
                        c = Coord.Coord(x - i, y)
                        self.move_bot(robot.color(), c)
                        break
        elif direction == Direction.Direction.SOUTH:
            for i in range(16):
                if x + i >= 15:
                    if s.check_case_to_stop(x + i, y, 'down'):
                        c = Coord.Coord(x + i, y)
                        self.move_bot(robot.color(), c)
                        break
        elif direction == Direction.Direction.EAST:
            for j in range(16):
                if y + j >= 0:
                    if s.check_case_to_stop(x, y + j, 'right'):
                        c = Coord.Coord(x, y + j)
                        self.move_bot(robot.color(), c)
                        break
        elif direction == Direction.Direction.WEST:
            for j in range(16):
                if y - j >= 0:
                    if s.check_case_to_stop(x, y - j, 'left'):
                        c = Coord.Coord(x, y - j)
                        self.move_bot(robot.color(), c)
                        break

    # Method to remove an object of the board at the end of the round
    def remove_object(self, game_object):
        for i in range(16):
            for j in range(16):
                if self._cases[i][j].has_game_object():
                    if self._cases[i][j].game_object == game_object:
                        self._cases[i][j].remove_game_object()

    # Method to replace the moved bots to their start position
    def reset_bot(self):
        for i in range(16):
            for j in range(16):
                if self._cases[i][j].has_bot():
                    robot = self._cases[i][j].bot
                    if (
                            robot.pos.x != robot.start_pos.x
                            or robot.pos.y != robot.start_pos.y
                    ):
                        robot.reset_pos()
                        self._cases[robot.start_pos.x][robot.start_pos.y].place_bot(robot)
                        self._cases[i][j].remove_bot()

    """def can_go_to_case(self, x_to_reach, y_to_reach, robot):
        for d in self._cases[robot.pos.x, robot.pos.y].destination.case:
            if d.pos.x == x_to_reach and d.pos.y == y_to_reach:
                return True
        return False"""
