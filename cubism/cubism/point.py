from collections import namedtuple

PointBase = namedtuple("PointBase", ('x', 'y'))
class Point(PointBase):
    def __new__(cls, x=0, y=0):
        self = super(Point, cls).__new__(cls, x, y)
        return self

    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.x + other, self.y + other)
        return self.__class__(self.x + other[0], self.y + other[1])

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.x - other, self.y - other)
        return self.__class__(self.x - other[0], self.y - other[1])
    
    def __mul__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.x * other, self.y * other)
        return self.__class__(self.x * other[0], self.y * other[1])
    
    def __div__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.x / other, self.y / other)
        return self.__class__(self.x / other[0], self.y / other[1])
    
    def __neg__(self):
        return self.__class__(-self.x, -self.y)


