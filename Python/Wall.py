class Wall:
    def __init__(self, direction):
        self._dir = direction

    @property
    def dir(self):
        return self._dir
