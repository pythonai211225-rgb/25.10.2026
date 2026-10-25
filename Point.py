from functools import total_ordering
from operator import index

# class Point
# - x: float
# - y: float
# + X { read-only}
# + Y { read-only}

# create point1 [x=9.44, y=-10]
# print(point1.X)
# print(point2.Y)

import math

@total_ordering # we write __eq__ and __lt__, it generates <=, >, >=
class Point:
    #-- ctor constructor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.__x + other, self.__y + other)
        elif not isinstance(other, Point):
            return NotImplemented        
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point.distance_from_origin(self) == Point.distance_from_origin(other)

    def __neq__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def distance_from_origin(point):
        return math.sqrt(point.__x **2 + point.__y**2)

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point.distance_from_origin(self) < Point.distance_from_origin(other)

    # gt

    def __len__(self):
        return Point.distance_from_origin(self)

    def __str__(self):
        return f"Point ({self.__x}, {self.__y})"

    def __repr__(self):
        return self.__str__()    

    def __getitem__(self, key):
        if key == 'x':
            return self.x
        elif key == 'y':
            return self.y
        elif key == 'distance':
            return Point.distance_from_origin(self)
        else:
            return NotImplemented

point1 = Point(9.44, -10)
print(f"Point ({point1.x}, {point1.y})")
# point1.x += 1 # Error
p1 = Point(4.51, -0.3)
p2 = Point(0.7, 1)
p3 = p1 + p2  #  p3 = Point(5.21, 0.7)
p4 = p1 - p2  #  p4 = Point(3.81, -1.3)
p5 = p1 + 5   #  p5 = Point(9.51, 4.7)

p2 = Point(0.7, 1)
p3 = Point(0.7, 1)
print(p2 == p3)  # implement __eq__
print(p2 != p3)  # implement __neq__

p4 = Point(3, 4)
p5 = Point(2.5, 3.5)
print(p4 < p5)  # implement __lt__
print(p4 > p5)  # implement __gt__
print(p4 >= p5)  # implement __ge__

print(len(p4))
print(p4)  # Point <address> --> Point(3, 4) -- implement __str__
print([p4, p3])  # implement __repr__

dict1 = {"x": 3, "y": 4, "distance": 5}
print(dict1["x"])
print(dict1["y"])
print(dict1["distance"])

print(p1["x"]) # __getitem__
print(p1["y"]) # __getitem__
print(p1["distance"])

print(Point.distance_from_origin(p3))

# for x in p4: __iter__
