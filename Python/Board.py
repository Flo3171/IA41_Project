import Case
import Coord
import Wall
import Direction
import GameObject
import Robot
import Destination
import random
import math

class Board:

    def __init__(self):
        # init the board
        self._cases = [[Case.Case(Coord.Coord(j, i)) for i in range(16)] for j in range(16)]
                        
        #self._caseDestinationCoord #à générer sous forme [i,j]
        #self._robots = []       #à générer sous forme [r1,r2,r3,r4]

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


        avaliableQuarter = [True, True, True, True]
        #put one template on each quarter map
        for i in range(4):

            template = random.randint(0, 15)

            while(avaliableQuarter[template % 4] == False):
                template = random.randint(0, 7)
            
            avaliableQuarter[template%4] = False
            print(template)

            if (template == 0):
                #template number 0
                self.put_wall(Coord.Coord(1, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(2, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 5), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 6), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(4, 1), i, GameObject.GameObject.RED_BALL, Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(2, 1), i, GameObject.GameObject.GREEN_BEACON, Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(6, 3), i, GameObject.GameObject.YELLOW_COIN, Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(4, 6), i, GameObject.GameObject.BLUE_RING, Direction.Direction.SOUTH_WEST)


            
            elif (template == 1):
                # template number 1
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 3), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 4), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(5, 1), i, GameObject.GameObject.GREEN_COIN, Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(1, 2), i, GameObject.GameObject.RED_RING, Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(6, 4), i, GameObject.GameObject.YELLOW_BALL, Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(2, 6), i, GameObject.GameObject.BLUE_BEACON, Direction.Direction.NORTH_EAST)

            elif (template == 2):
                # template number 2
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 4), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 5), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(5, 2), i, GameObject.GameObject.BLUE_COIN, Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(2, 4), i, GameObject.GameObject.GREEN_BALL, Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(7, 5), i, GameObject.GameObject.RED_BEACON, Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(1, 6), i, GameObject.GameObject.YELLOW_RING, Direction.Direction.NORTH_WEST)

            elif (template == 3):
                # template number 3
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.WEST, i)
 
                self.put_wall(Coord.Coord(0, 6), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 7), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(6, 1), i, GameObject.GameObject.BLUE_BALL, Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(1, 3), i, GameObject.GameObject.YELLOW_BEACON, Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(5, 4), i, GameObject.GameObject.GREEN_RING, Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(2, 5), i, GameObject.GameObject.RED_COIN, Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(7, 5), i, GameObject.GameObject.VORTEX, Direction.Direction.SOUTH_EAST)

            elif (template == 4):
                # template number 4
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 5), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 6), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(6, 1), i, GameObject.GameObject.YELLOW_COIN, Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(1, 2), i, GameObject.GameObject.GREEN_BEACON, Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(6, 5), i, GameObject.GameObject.BLUE_RING, Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(3, 6), i, GameObject.GameObject.RED_BALL, Direction.Direction.SOUTH_WEST)

            elif (template == 5):
                # template number 5
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 4), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 5), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(2, 1), i, GameObject.GameObject.YELLOW_BALL, Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(6, 3), i, GameObject.GameObject.BLUE_BEACON, Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(4, 5), i, GameObject.GameObject.RED_RING, Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(1, 6), i, GameObject.GameObject.GREEN_COIN, Direction.Direction.SOUTH_WEST)

            elif (template == 6):
                # template number 6
                self.put_wall(Coord.Coord(3, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 5), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 6), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(1, 1), i, GameObject.GameObject.RED_BEACON, Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(6, 2), i, GameObject.GameObject.GREEN_BALL, Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(2, 4), i, GameObject.GameObject.BLUE_COIN, Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(7, 5), i, GameObject.GameObject.YELLOW_RING, Direction.Direction.NORTH_WEST)

            elif (template == 7):
                # template number 7
                self.put_wall(Coord.Coord(4, 0), Direction.Direction.EAST, i)
                self.put_wall(Coord.Coord(5, 0), Direction.Direction.WEST, i)

                self.put_wall(Coord.Coord(0, 4), Direction.Direction.SOUTH, i)
                self.put_wall(Coord.Coord(0, 5), Direction.Direction.NORTH, i)

                self.put_object(Coord.Coord(2, 1), i, GameObject.GameObject.RED_COIN, Direction.Direction.SOUTH_EAST)
                self.put_object(Coord.Coord(1, 3), i, GameObject.GameObject.GREEN_RING, Direction.Direction.SOUTH_WEST)
                self.put_object(Coord.Coord(6, 4), i, GameObject.GameObject.YELLOW_BEACON, Direction.Direction.NORTH_WEST)
                self.put_object(Coord.Coord(5, 6), i, GameObject.GameObject.BLUE_BALL, Direction.Direction.NORTH_EAST)
                self.put_object(Coord.Coord(3, 7), i, GameObject.GameObject.VORTEX, Direction.Direction.SOUTH_EAST)


            


    def put_wall(self, coord, direction, rotation):
        if( coord.x >= 0 & coord.x < 16 & coord.y >= 0 & coord.y < 16):
            newCord = coord.rotate(rotation)
            self._cases[newCord.x][newCord.y].add_wall(Wall.Wall(Direction.get_n_adjacent(direction, rotation)))

    def put_object(self, coord, rotation, obj, direction):
        newCord = coord.rotate(rotation)
        self._cases[newCord.x][newCord.y].add_game_object(obj)
        
        if(direction == Direction.Direction.NORTH_EAST):
            self.put_wall(coord, Direction.Direction.NORTH, rotation)
            self.put_wall(Coord.Coord(coord.x, coord.y-1), Direction.Direction.SOUTH, rotation)

            self.put_wall(coord, Direction.Direction.EAST, rotation)
            self.put_wall(Coord.Coord(coord.x + 1,  coord.y), Direction.Direction.WEST, rotation)
        
        elif(direction == Direction.Direction.SOUTH_EAST):
            self.put_wall(Coord.Coord(coord.x, coord.y + 1), Direction.Direction.NORTH, rotation)
            self.put_wall(coord, Direction.Direction.SOUTH, rotation)

            self.put_wall(coord, Direction.Direction.EAST, rotation)
            self.put_wall(Coord.Coord(coord.x + 1,  coord.y), Direction.Direction.WEST, rotation)

        elif(direction == Direction.Direction.SOUTH_WEST):
            self.put_wall(Coord.Coord(coord.x, coord.y + 1), Direction.Direction.NORTH, rotation)
            self.put_wall(coord, Direction.Direction.SOUTH, rotation)

            self.put_wall(Coord.Coord(coord.x - 1, coord.y), Direction.Direction.EAST, rotation)
            self.put_wall(coord, Direction.Direction.WEST, rotation)

        elif(direction == Direction.Direction.NORTH_WEST):
            self.put_wall(coord, Direction.Direction.NORTH, rotation)
            self.put_wall(Coord.Coord(coord.x, coord.y - 1), Direction.Direction.SOUTH, rotation)

            self.put_wall(Coord.Coord(coord.x - 1, coord.y), Direction.Direction.EAST, rotation)
            self.put_wall(coord, Direction.Direction.WEST, rotation)
