class Destination:
    def __init__(self, direction, case):
        self._direction = direction
        self._case = case

    @property
    def direction(self):
        return self._direction

    @property
    def case(self):
        return self._case
