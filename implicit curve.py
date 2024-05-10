import numpy as np
import matplotlib.pyplot as plt

def implicit_curve(equation, xlim=(-10, 10), ylim=(-10, 10), num_points=1000):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = np.linspace(ylim[0], ylim[1], num_points)
    X, Y = np.meshgrid(x, y)

    Z = eval(equation)  

    plt.contour(X, Y, Z, [0], colors='b')  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
    
equation = 'X**2 + Y**2 - 16'  
implicit_curve(equation)