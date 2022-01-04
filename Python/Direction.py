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


# used to return the opposite direction of the given one : NORTH -> SOUTH, SOUTH_WEST -> NORTH_EAST
def get_opposite(direction):
    opposite = [element * -1 for element in direction.value]
    for direction in Direction:
        if opposite == direction.value:
            return direction


# use tu return the next direction with à pi/2 clockwise rotation : NORTH -> EAST, SOUTH_EAST -> SOUTH_WEST
def get_adjacent(direction):
    if direction.value[1] == -1 or direction.value[0] == -1:
        adjacent = [
            int(math.cos(math.acos(direction.value[0]) - (math.pi / 2))),
            int(math.sin(math.asin(direction.value[1]) - (math.pi / 2))),
        ]
    else:
        adjacent = [
            int(math.cos(math.acos(direction.value[0]) + (math.pi / 2))),
            int(math.sin(math.asin(direction.value[1]) + (math.pi / 2))),
        ]

    for direction in Direction:
        if adjacent == direction.value:
            return direction


def get_n_adjacent(direction, rotate):
    if rotate == 0:
        return direction
    else:
        return get_n_adjacent(get_adjacent(direction), rotate - 1)


def get_ordinal_direction_list():
    return [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
