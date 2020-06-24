import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from euler import *
from attractor import *




if __name__ == '__main__':
    N = 3000
    print("Введите начальную точку (Если вы собираетесь выбрать аттрактор Лоренца, то лучше не начинать с начала координат (0, 0, 0))")
    x_0 = float(input("x_0 = "))
    y_0 = float(input("y_0 = "))
    z_0 = float(input("z_0 = "))

    T = float(input("Введите конечный момент времени T = "))

    attractor_choice = int(input("Аттрактор Рёсслера == 0\nАттрактор Лоренца == 1\nВы выбираете аттрактор == "))

    if attractor_choice == 0:
        print(
"""
Аттрактор Рёсслера имеет вид:
x` = -y-z
y` = x + a * y
z` = b + z * (x - c)
"""
        )

        print("Рекомендуемые параметры a = 0.2  b = 0.2  c = 6")

        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))

        attractor = Ressler(a, b, c)
    else:
        print(
"""
Аттрактор Лоренца имеет вид:
x` = a * (y - x)
y` = x * (b - z) - y
z` = x * y - c * z
"""
        )

        print("Рекомендуемые параметры a = 5  b = 15 c = 1")

        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))

        attractor = Lorenz(a, b, c)

    method_choice = int(input("Метод Эйлера == 0\nМетод Рунге-Кутты == 1\nВы выбираете метод == "))

    start_time = time.time()
    if method_choice == 1:
        print("Был выбран метод Рунге-Кутты")
        result = Runge(attractor, Vector3(x_0, y_0, z_0), T, N)
    else:
        print("Был выбран метод Эйлера")
        result = Euler(attractor, Vector3(x_0, y_0, z_0), T, N)

    x, y, z = result.get_path()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='parametric curve')

    print("Время выполнения программы == ", time.time() - start_time)

    plt.show()
