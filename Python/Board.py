import Case
import Coord
import Wall
import Direction
import GameObject
import Robot
import Destination

class Board:

    def __init__(self):
        # init the board
        self._cases = [[Case.Case(Coord.Coord(0,0))] * 16 for i in range(16)]
        #set corectly all the cordinate
        for j in range(16):
            for j in range(16):
                for i in range(16):

                    #expt the four case in the center because they are not usable

                    if (j < 7 or j > 8) or (i < 7 or i > 8):
                        self._cases[i][j] = Case.Case(Coord.Coord(i, j)
                        )

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


    
