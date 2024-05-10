import matplotlib.pyplot as plt

# Original triangle vertices
x = [0, 2, 3, 0]
y = [0, 0, 1, 0]

# Reflection factors
sx = 1
sy = -1

# Perform reflection
reflected_x = [vertex * sx for vertex in x]
reflected_y = [vertex * sy for vertex in y]

# Plotting the original triangle
plt.plot(x, y, 'b-', label='Original')

# Plotting the reflected triangle
plt.plot(reflected_x, reflected_y, 'r--', label='Reflected')

# Set axis limits
plt.xlim(min(x + reflected_x) - 1, max(x + reflected_x) + 1)
plt.ylim(min(y + reflected_y) - 1, max(y + reflected_y) + 1)

# Add legend and labels
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

# Display the plot
plt.show()