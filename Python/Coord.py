import Direction

class Coord:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "x= %d, y= %d" % (self._x, self._y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    def is_in_map(self):
        return 0 <= self.x < 16 and 0 <= self.y < 16

    def add_direction(self, direction):
        return Coord(self.x + Direction.get_x(direction), self.y + Direction.get_y(direction))

    def rotate(self, angle):

        angle = angle % 4
        x_a = self.x - 7.5
        y_a = 7.5 - self.y

        if angle == 0:
            cos = 1
            sin = 0
        elif angle == 1:
            cos = 0
            sin = -1
        elif angle == 2:
            cos = -1
            sin = 0
        else:
            cos = 0
            sin = 1

        x_b = x_a * cos - y_a * sin
        y_b = y_a * cos + x_a * sin

        x_c = int(x_b + 7.5)
        y_c = int(7.5 - y_b)

        return Coord(x_c, y_c)
