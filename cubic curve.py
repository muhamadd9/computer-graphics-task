import numpy as np
import matplotlib.pyplot as plt

def cubic_curve(a, b, c, d, xlim=(-10, 10), ylim=(-10, 10), num_points=1000):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = a * x**3 + b * x**2 + c * x + d

    plt.plot(x, y)  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

a = 1
b = -2
c = -1
d = 2
cubic_curve(a, b, c, d)