import math

class CN:
    r = 0;
    i = 0;

    def __init__(self, real, imag):
        self.r = real
        self.i = imag

    def mag(self):
        return math.sqrt(self.r**2+self.i**2)

    def __add__(self, other):
        return CN(self.r+other.r, self.i + other.i)

    def __sub__(self, other):
        return CN(self.r-other.r, self.i-other.i)

    def __mul__(self, other):
        return CN(self.r*other.r - (self.i*other.i), self.i*other.r + (self.r*other.i))

    def __truediv__(self, other):
        first = self.r*other.r + self.i*other.i
        second = self.i*other.real - self.r*other.i
        b = other.r**2 + other.i**2
        return CN(first/b, second/b)

    def __eq__(self, other):
        if(self.r == other.r and self.i == other.i):
            return True
        else:
            return False

    def conjugate(self):
        return CN(self.r, -self.i)

    def show(self):
        if self.i < 0:
            return str(self.r) + str(self.i) + "i"
        else:
            return str(self.r) + "+" + str(self.i) + "i"

