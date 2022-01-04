class Move:

    def __init__(self, robot_color, direction):
        self._robot_color = robot_color
        self._direction = direction

    def robot_color(self):
        return self._robot_color

    def direction(self):
        return self._direction
