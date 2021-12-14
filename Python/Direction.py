from enum import Enum
import math

class Direction(Enum):
    NORTH = [0, -1]
    NORTH_EAST = [1, 1]
    EAST = [1, 0]
    SOUTH_EAST = [1, -1]
    SOUTH = [0, 1]
    SOUTH_WEST = [-1, -1]
    WEST = [-1, 0]
    NORTH_WEST = [-1, 1]


# used to get x and y offset of a direction 
def get_x(direction):
    return direction.value[0]

def get_y(direction):
    return direction.value[1]

# used to return the oppostie direction of the givene one : NORTH -> SOUTH, SOUTH_WEST -> NORTH_EAST
def get_opposite(direction):
    opposite = [element * -1 for element in direction.value]
    for dir in Direction:
        if opposite == dir.value:
            return dir

# use tu return the next direction with à pi/2 clockwise rotation : NORTH -> EAST, SOUTH_EAST -> SOUTH_WEST
def get_adjacent(direction):
    if direction.value[1] == -1 or direction.value[0] == -1:
        adjcent = [
            int(math.cos(math.acos(direction.value[0]) - (math.pi / 2))),
            int(math.sin(math.adin(direction.value[1]) - (math.pi / 2))),
        ]
    else:
        adjacent = [
            int(math.cos(math.acos(direction.value[0]) + (math.pi / 2))),
            int(math.sin(math.asin(direction.value[1]) + (math.pi / 2))),
        ]

    for dir in Direction:
        if adjacent == dir.value:
            return dir
