class Robot:
    def __init__(self, color, start_pos):
        self._color = color
        self._pos = start_pos
        self._startPos = start_pos


    def color(self):
        return self._color

    @property
    def start_pos(self):
        return self._startPos


    def pos(self):
        return self._pos

    def move(self, coord):
        self._pos = coord

    def reset_pos(self):
        self._pos = self._startPos
"""
    def __eq__(self, other):
        if (self._color == other._color) and (self._pos == other._pos) and (self._startPos == other._startPos):
            return True
"""