from vector3 import *
import numpy as np


class Euler:
    def __init__(self, attractor, start, T, N):
        self.path = []
        self.h = T / N
        self.T = T
        self.N = N

        self.start = start

        self.attractor = attractor

        self.calculate_attractor()

    def calculate_attractor(self):
        x = self.start.x
        y = self.start.y
        z = self.start.z

        self.path.append(Vector3(x, y, z))

        for i in range(self.N + 1):
            t = i * self.h

            x += self.h * self.attractor.p(t, x, y, z)
            y += self.h * self.attractor.q(t, x, y, z)
            z += self.h * self.attractor.r(t, x, y, z)

            self.path.append(Vector3(x, y, z))

    def get_path(self):
        arr_x = np.array([])
        arr_y = np.array([])
        arr_z = np.array([])

        for vector in self.path:
            arr_x = np.append(arr_x, vector.x)
            arr_y = np.append(arr_y, vector.y)
            arr_z = np.append(arr_z, vector.z)

        return arr_x, arr_y, arr_z


class Runge:
    def __init__(self, attractor, start, T, N):
        self.path = []
        self.h = T / N
        self.T = T
        self.N = N

        self.start = start

        self.attractor = attractor

        self.calculate_attractor()

    def get_path(self):
        arr_x = np.array([])
        arr_y = np.array([])
        arr_z = np.array([])

        for vector in self.path:
            arr_x = np.append(arr_x, vector.x)
            arr_y = np.append(arr_y, vector.y)
            arr_z = np.append(arr_z, vector.z)

        return arr_x, arr_y, arr_z

    def calculate_attractor(self):
        x = self.start.x
        y = self.start.y
        z = self.start.z

        for i in range(1, self.N + 1):
            t = i * self.h

            k11 = self.h * self.attractor.p(t, x, y, z)
            k12 = self.h * self.attractor.q(t, x, y, z)
            k13 = self.h * self.attractor.r(t, x, y, z)

            k21 = self.h * self.attractor.p(t + self.h / 2, x + k11 / 2, y + k12 / 2, z + k13 / 2)
            k22 = self.h * self.attractor.q(t + self.h / 2, x + k11 / 2, y + k12 / 2, z + k13 / 2)
            k23 = self.h * self.attractor.r(t + self.h / 2, x + k11 / 2, y + k12 / 2, z + k13 / 2)

            k31 = self.h * self.attractor.p(t + self.h / 2, x + k21 / 2, y + k22 / 2, y + k23 / 2)
            k32 = self.h * self.attractor.q(t + self.h / 2, x + k21 / 2, y + k22 / 2, y + k23 / 2)
            k33 = self.h * self.attractor.r(t + self.h / 2, x + k21 / 2, y + k22 / 2, y + k23 / 2)

            k41 = self.h * self.attractor.p(t + self.h, x + k31, y + k32, z + k33)
            k42 = self.h * self.attractor.q(t + self.h, x + k31, y + k32, z + k33)
            k43 = self.h * self.attractor.r(t + self.h, x + k31, y + k32, z + k33)

            x += (k11 + 2*k21 + 2*k31 + k41) / 6
            y += (k12 + 2*k22 + 2*k32 + k42) / 6
            z += (k13 + 2*k23 + 2*k33 + k43) / 6

            self.path.append(Vector3(x, y, z))