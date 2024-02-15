import numpy as np
import matplotlib.pyplot as plt

def rosenbrock(x, y):
    a = 1
    b = 100
    return (a - x)**2 + b * (y - x**2)**2

x = np.linspace(-2, 2, 100)
y = np.linspace(-1, 3, 100)
x, y = np.meshgrid(x, y)
z = rosenbrock(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Label axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('Rosenbrock Function')
plt.show()