class Objective:

    def __init__(self, coord, game_object):
        self._coord = coord
        self._game_object = game_object

    @property
    def coord(self):
        return self._coord

    @property
    def game_object(self):
        return self._game_object
