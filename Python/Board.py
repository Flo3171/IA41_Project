import Case
import Coord
import Wall
import Direction
import GameObject
import Robot
import Destination
from random import randrange

class Board:

    def __init__(self):
        # init the board
        self._cases = [[Case.Case(Coord.Coord(0,0))] * 16 for i in range(16)]
        #set corectly all the cordinate
        for j in range(16):
            for i in range(16):

                #expt the four case in the center because they are not usable
                if (j < 7 or j > 8) or (i < 7 or i > 8):
                    self._cases[i][j] = Case.Case(Coord.Coord(i, j))

    def genreate_board(self):
        #TODO find a way to generate the board used template like in the orginal game or random génration

        for j in range(16):

            #put the wall around the map
            self._cases[j][0].add_wall(Wall.Wall(Direction.Direction.NORTH))
            self._cases[0][j].add_wall(Wall.Wall(Direction.Direction.WEST))
            self._cases[j][15].add_wall(Wall.Wall(Direction.Direction.SOUTH))
            self._cases[15][j].add_wall(Wall.Wall(Direction.Direction.EAST))

            for i in range(16):

                #put the wall around the central block
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

        #put one template on each quarter map
        for i in range(4):
            template = randrange(1)
            if (template == 0):
                self.put_wall(1, 0, Direction.Direction.EAST, i)
                self.put_wall(2, 0, Direction.Direction.WEST, i)

                self.put_wall(0, 5, Direction.Direction.SOUTH, i)
                self.put_wall(0, 6, Direction.Direction.NORTH, i)

                self.put_wall(1, 1, Direction.Direction.SOUTH, i)
                self.put_wall(1, 2, Direction.Direction.NORTH, i)
                self.put_wall(1, 2, Direction.Direction.EAST, i)
                self.put_wall(2, 2, Direction.Direction.WEST, i)
                self.put_object(2, 1, i, GameObject.GameObject.GREEN_BEACON)

                self.put_wall(4, 0, Direction.Direction.SOUTH, i)
                self.put_wall(4, 1, Direction.Direction.NORTH, i)
                self.put_wall(3, 1, Direction.Direction.EAST, i)
                self.put_wall(4, 1, Direction.Direction.WEST, i)
                self.put_object(4, 1, i, GameObject.GameObject.RED_BALL)

                self.put_wall(6, 3, Direction.Direction.EAST, i)
                self.put_wall(7, 3, Direction.Direction.WEST, i)
                self.put_wall(6, 3, Direction.Direction.SOUTH, i)
                self.put_wall(6, 4, Direction.Direction.NORTH, i)
                self.put_object(6, 3, i, GameObject.GameObject.YELLOW_COIN)

                self.put_wall(4, 6, Direction.Direction.WEST, i)
                self.put_wall(3, 6, Direction.Direction.EAST, i)
                self.put_wall(4, 6, Direction.Direction.SOUTH, i)
                self.put_wall(4, 7, Direction.Direction.NORTH, i)
                self.put_object(4, 6, i, GameObject.GameObject.BLUE_RING)


            
            elif (template == 1):
                a=a
                #self._cases[]

    def put_wall(self, x, y, direction, rotation):
        self._cases[x.rotate(rotation)][y.rotate(rotation)].add_wall(Wall.Wall(Direction.get_n_adjacent(direction, rotation)))

    def put_object(self, x, y, rotation, obj):
        self._cases[x.rotate(rotation)][y.rotate(rotation)].add_game_object(obj)