class Point:

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def reflect_x(self):
        return self.x, self.y * -1

    def slope_from_origin(self):
        return self.y / self.x

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


print(Point(4, 10).slope_from_origin())
