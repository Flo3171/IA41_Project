import Coord

class Robot:
    def __init__(self, color, startPos):
        self._color = color
        self._pos = startPos
        self._startPos = startPos

    @property
    def color(self):
        return self._color

    @property
    def startPos(self):
        return self._startPos

    @property
    def pos(self):
        return self._pos

    @property
    def image(self):
        return self._image

    def mouve(self, coord):
        self._pos = coord

    def reset_pos(self):
        self._pos = self._startPos


