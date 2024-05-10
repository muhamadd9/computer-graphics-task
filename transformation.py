#Transformation Tasks
import matplotlib.pyplot as plt
import math

# Original line vertices
x = [0, 5]
y = [0, 5]

# Rotation angle in degrees
angle = -45

# Convert angle to radians
angle_rad = math.radians(angle)

# Perform rotation
rotated_x = [vertex * math.cos(angle_rad) - y[i] * math.sin(angle_rad) for i, vertex in enumerate(x)]
rotated_y = [vertex * math.sin(angle_rad) + y[i] * math.cos(angle_rad) for i, vertex in enumerate(x)]

# Plotting the original line
plt.plot(x, y, 'b-', label='Original')

# Plotting the rotated line
plt.plot(rotated_x, rotated_y, 'r--', label='Rotated')

# Set axis limits
plt.xlim(min(x + rotated_x) - 1, max(x + rotated_x) + 1)
plt.ylim(min(y + rotated_y) - 1, max(y + rotated_y) + 1)

# Add legend and labels
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

# Display the plot
plt.show()