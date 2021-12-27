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

    @property
    def game_object(self):
        return self.gameObject

    def add_game_object(self, obj):
        self._gameObject = obj

    def remove_game_object(self):
        self._gameObject = None
    
    def has_game_object(self):
        if self._gameObject == None:
            return False
        else:
            return True

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

        

    @property
    def bot(self):
        return self._bot

    def has_bot(self):
        if self._bot == None:
            return False
        else: 
            return True
    
    @property
    def destination(self):
        return self._destination

    def add_destination(self, destination):
        self._destination.append(destination)

    def reset_destinations(self):
        self._destination = []

    def place_bot(self, bot):
        self._bot = bot

    def remove_bot(self):
        self._bot

    