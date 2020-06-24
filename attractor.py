import numpy as np

class Ressler:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def p(self, t, x, y, z):
        return -y - z

    def q(self, t, x, y, z):
        return x + self.a * y

    def r(self, t, x, y, z):
        return self.b + z * (x - self.c)


class Lorenz:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def p(self, t, x, y, z):
        return self.a * (y - x)

    def q(self, t, x, y, z):
        return x * (self.b - z) - y

    def r(self, t, x, y, z):
        return x * y - self.c * z
