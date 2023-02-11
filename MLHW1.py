import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def find_plane(p1, p2, p3):
  # create vectors
  v1 = p2 - p1
  v2 = p3 - p1

  # find the normal vector to the plane
  normal = np.cross(v1, v2)

  # find the equation of the plane
  d = -np.dot(normal, p1)
  return normal, d

def verify_plane(normal, d, p):
  # calculate the distance from the point to the plane
  dist = np.dot(normal, p) + d

  # return True if the distance is zero, False otherwise
  return np.isclose(dist, 0)

def plot_plane(normal, d):
  # create grid of points
  x, y = np.meshgrid(range(-5,5), range(-5,5))

  # calculate the corresponding z values
  z = (-normal[0]*x - normal[1]*y - d) / normal[2]

  # plot the plane
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_surface(x, y, z)
  plt.show()

# test the functions
p1 = np.array([1, 0, -1])
p2 = np.array([3, 1, 4])
p3 = np.array([3, -2, 0])
normal, d = find_plane(p1, p2, p3)
print(f'The equation of the plane is {normal[0]}x + {normal[1]}y + {normal[2]}z + {d} = 0')

print(f'p1 lies on the plane: {verify_plane(normal, d, p1)}')
print(f'p2 lies on the plane: {verify_plane(normal, d, p2)}')
print(f'p3 lies on the plane: {verify_plane(normal, d, p3)}')

plot_plane(normal, d)