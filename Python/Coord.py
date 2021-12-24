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
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y = y

    def rotate(self, angle):

        angle = angle % 4
        xA = self.x - 7.5
        yA = 7.5 - self.y

        if(angle == 0):
            cos = 1
            sin = 0
        elif(angle == 1):
            cos = 0
            sin = -1
        elif(angle == 2):
            cos = -1
            sin =  0
        elif(angle == 3):
            cos = 0
            sin = 1
        
        xB = xA*cos - yA*sin
        yB = yA*cos + xA* sin

        xC = xB + 7.5
        yC = 7.5 - yB 


        return Coord(xC, yC)