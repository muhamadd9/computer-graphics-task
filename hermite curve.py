import numpy as np
import matplotlib.pyplot as plt

def hermite_curve(control_points, tangent_vectors, num_points=100):
    t = np.linspace(0, 1, num_points)
    n = len(control_points)
    curve = np.zeros((num_points, 2))

    for i in range(n - 1):
        p0, p1 = control_points[i], control_points[i + 1]
        t0, t1 = tangent_vectors[i], tangent_vectors[i + 1]
        h00 = 2 * t**3 - 3 * t**2 + 1
        h10 = t**3 - 2 * t**2 + t
        h01 = -2 * t**3 + 3 * t**2
        h11 = t**3 - t**2

        x = h00 * p0[0] + h10 * t0[0] + h01 * p1[0] + h11 * t1[0]
        y = h00 * p0[1] + h10 * t0[1] + h01 * p1[1] + h11 * t1[1]

        curve += np.column_stack((x, y))

    plt.plot(curve[:, 0], curve[:, 1]) 
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


control_points = [(0, 0), (1, 2), (3, -1), (4, 3)]  # Control 
tangent_vectors = [(1, 1), (2, -1), (-1, -2), (3, 1)]  # Tangent 
hermite_curve(control_points, tangent_vectors)