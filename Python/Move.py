class Move:

    def __init__(self, robot, direction):
        self._robot = robot
        self._direction = direction

    def robot(self):
        return self._robot

    def direction(self):
        return self._direction
