class Case:
    def __init__(self, coord):
        self._coord = coord
        self._walls = []
        self._gameObject = None
        self._bot = None
        self._destination = []

    @property
    def coord(self):
        return self._coord


    def game_object(self):
        return self._gameObject

    def add_game_object(self, obj):
        self._gameObject = obj

    def remove_game_object(self):
        self._gameObject = None

    def has_game_object(self):
        return self._gameObject is not None

    @property
    def walls(self):
        return self._walls

    def add_wall(self, wall):
        self._walls.append(wall)

    def has_walls(self):
        if not self._walls:
            return False
        else:
            return True

    def has_walls_in_dir(self, dir):
        for w in self._walls:
            if dir == w.dir:
                return True
        return False



    def bot(self):
        return self._bot

    def has_bot(self):
        return self._bot is not None

    @property
    def destinations(self):
        return self._destination

    def destination(self, direction):
        print(len(self._destination))
        for i in range(len(self._destination)):
            if self._destination[i].direction == direction:
                return self._destination[i]

    def add_destination(self, destination):
        self._destination.append(destination)

    def reset_destinations(self):
        self._destination = []

    def place_bot(self, bot):
        self._bot = bot

    def remove_bot(self):
        self._bot = None