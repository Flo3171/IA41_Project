class Robot:
    def __init__(self, color, start_pos):
        self._color = color
        self._pos = start_pos
        self._startPos = start_pos

    def __eq__(self, other):
        return self._color == other.color() and self._pos == other.pos() and self._startPos == other.startPos()


    def color(self):
        return self._color

    @property
    def start_pos(self):
        return self._startPos

    @property
    def pos(self):
        return self._pos

    def move(self, coord):
        self._pos = coord

    def reset_pos(self):
        self._pos = self._startPos
