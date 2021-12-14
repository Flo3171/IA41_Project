class Wall:
    def __init__(self, dir):
        self._dir = dir

    @property
    def dir(self):
        return self._dir