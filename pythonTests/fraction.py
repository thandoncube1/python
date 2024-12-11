""" Working on a fraction object """
class Fraction(object):
    """
        A number represented as a fraction
    """
    def __init__(self, num: int, denom: int):
        self.num = num
        self.denom = denom

    def __str__(self):
        """ Returns a string representation of self """
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        """ Returns the new fraction representing the addition """
        top = self.num*other.denom + self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        """ Returns the new fraction representing the addition """
        top = self.num*other.denom - self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom

    def inverse(self):
        return Fraction(self.denom, self.num)


def main():
    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b # c is a Fraction object
    print(c)
    print(float(c))
    print(Fraction.__float__(c))
    print(float(b.inverse()))

if __name__ == "__main__":
    main()