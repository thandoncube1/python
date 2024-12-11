# Coordinate object - Code that defines a point (x, y) in a 2-D Plane

class Coordinate(object):
    # define attributes here...
    """Data and procedures that are related to the class"""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other):
        """
            Takes two coordinate objects to calculate the distance
            - Self is one object
            - Other is another defined object
            :self - Object
            :other - Object
        """
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"


def main():
    c = Coordinate(3.0, 4.0)
    origin = Coordinate(0.0, 0.0)
    print(c.x)
    print(origin.x)
    # print(Coordinate.distance(c, origin)) - This is a little
    # cumbersome
    print(c, type(c), Coordinate, type(Coordinate))
    print(c.distance(origin))

if __name__ == "__main__":
    main()