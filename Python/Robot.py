class Robot:
    def __init__(self, color, start_pos):
        self._color = color
        self._pos = start_pos
        self._startPos = start_pos

    @property
    def color(self):
        return self._color

    @property
    def start_pos(self):
        return self._startPos

    @property
    def pos(self):
        return self._pos

    @property
    def image(self):
        return self._image

    def move(self, coord):
        self._pos = coord

    def reset_pos(self):
        self._pos = self._startPos
