import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def dot_product(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))

def cross_product(v1, v2):
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

def find_plane(p1, p2, p3):
    # create vectors
    v1 = [x2 - x1 for x1, x2 in zip(p1, p2)]
    v2 = [x2 - x1 for x1, x2 in zip(p1, p3)]

    # find the normal vector to the plane
    normal = cross_product(v1, v2)

    # find the equation of the plane
    d = -dot_product(normal, p1)
    return normal, d

def verify_plane(normal, d, p):
    # calculate the distance from the point to the plane
    dist = dot_product(normal, p) + d

    # return True if the distance is zero, False otherwise
    return abs(dist) < 1e-6

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
p1 = [1, 1, 1]
p2 = [2, 2, 2]
p3 = [1, 2, 3]
normal, d = find_plane(p1, p2, p3)
print(f'The equation of the plane is {normal[0]}x + {normal[1]}y + {normal[2]}z + {d} = 0')

print(f'p1 lies on the plane: {verify_plane(normal, d, p1)}')
print(f'p2 lies on the plane: {verify_plane(normal, d, p2)}')
print(f'p3 lies on the plane: {verify_plane(normal, d, p3)}')

plot_plane(normal, d)
