import Case
import Coord
import Wall
import Direction

class BoardQuart :
    def __init__(self, id, postition):
        self._case = [[Case.Case(Coord.Coord(0,0))] * 8 for i in range(8)]
        
