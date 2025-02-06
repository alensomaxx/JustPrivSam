"""
Geometric Transformation: Scaling a Rectangle”, or if you want something shorter:

🔹 Rectangle Transformer
🔹 Matrix Transform Plotter
🔹 Affine Transformation Demo
🔹 2D Shape Transformer

"""



import numpy as np
import matplotlib.pyplot as plt

# Define the original points of a rectangle
D = np.array([[2,1], [2,6], [7,6], [7,1]])

# Define a transformation matrix (Example: Scaling by 2)
T = np.array([[2, 0], [0, 3]])  # This scales x by 2 and y by 3

# Apply the transformation correctly
D_t = np.dot(D, T)  # D * T performs matrix multiplication

# Plot the original shape
plt.plot(np.append(D[:, 0], D[0, 0]), np.append(D[:, 1], D[0, 1]), color='blue', label="Original")

# Plot the transformed shape
plt.plot(np.append(D_t[:, 0], D_t[0, 0]), np.append(D_t[:, 1], D_t[0, 1]), color='red', linestyle='dashed', label="Transformed")

plt.legend()
plt.show()
