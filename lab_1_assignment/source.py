import numpy as np
import math
from enum import Enum
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def custom_transformation(transformation_matrix, my_object) -> np.array:
    result = []

    for vector in my_object:
        result.append(np.dot(transformation_matrix, vector))
    return np.array(result)

def mirror_with_respect_to_XY_plane_3d(my_object) -> np.array:
    mirror_matrix = np.eye(3)

    mirror_matrix[2][2] = -1

    result = []
    for vector in my_object:
        result.append(np.dot(mirror_matrix, vector))

    return np.array(result)


def mirror_with_respect_to_axis_2d(axis, my_object) -> np.array:
    scale_matrix = np.eye(2)

    if axis == axis.X_axis:
        scale_matrix[1][1] = -1
    elif axis == axis.Y_axis:
        scale_matrix[0][0] = -1

    result = []
    for vector in my_object:
        result.append(np.dot(scale_matrix, vector))
    return np.array(result)


def change_scale(coefficient, my_object, dimension) -> np.array:
    scale_matrix = np.eye(dimension)

    for index in range(dimension):
        scale_matrix[index][index] = coefficient

    result = []
    for vector in my_object:
        result.append(np.dot(scale_matrix, vector))

    return np.array(result)



def rotate_2d_counter_clockwise(degree, my_object) -> np.array:
    radian_amount = degree / 57
    rotation_matrix_2d = np.array([[math.cos(radian_amount), -math.sin(radian_amount)],
                                   [math.sin(radian_amount), math.cos(radian_amount)]])
    result = []
    for vector in my_object:
        result.append(np.dot(rotation_matrix_2d, vector))

    return np.array(result)


class Axis(Enum):
    X_axis = 1
    Y_axis = 2
    Z_axis = 3

def initialize_plot_window_3d(x_lim=(-10, 10), y_lim=(-10, 10), z_lim=(-10, 10), x_scale=1, y_scale=1, z_scale=1, title=''):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)
    ax.set_zlim(z_lim)
    ax.set_xticks(np.arange(x_lim[0], x_lim[1] + 1, x_scale))
    ax.set_yticks(np.arange(y_lim[0], y_lim[1] + 1, y_scale))
    ax.set_zticks(np.arange(z_lim[0], z_lim[1] + 1, z_scale))
    ax.grid()
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title(title)
    return fig, ax


def plot_vectors_3d(vectors, ax, title, x_scale, y_scale, z_scale):
    # Clear previous content
    ax.cla()

    # Plot the vectors using the quiver function
    ax.quiver(np.zeros(len(vectors)), np.zeros(len(vectors)), np.zeros(len(vectors)),
              vectors[:, 0], vectors[:, 1], vectors[:, 2])

    # Set the grid scale
    ax.set_xticks(np.arange(-5, 6, x_scale))
    ax.set_yticks(np.arange(-5, 6, y_scale))
    ax.set_zticks(np.arange(-5, 6, z_scale))

    # Add grid and labels
    ax.grid()
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title(title)

def initialize_plot_window(x_lim=(-10, 10), y_lim=(-5, 5), x_scale=1, y_scale=1):
    fig, ax = plt.subplots()
    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)
    ax.set_xticks(np.arange(x_lim[0], x_lim[1] + 1, x_scale))  # generates a sequence for ticks
    ax.set_yticks(np.arange(y_lim[0], y_lim[1] + 1, y_scale))
    ax.grid()
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    return fig, ax


def plot_vectors(vectors, ax, title, x_scale, y_scale):
    # Clear previous content
    ax.cla()

    # Plot the vectors using the quiver function
    ax.quiver(np.zeros(len(vectors)), np.zeros(len(vectors)), vectors[:, 0], vectors[:, 1], angles='xy',
              scale_units='xy', scale=1)

    # Set the grid scale
    ax.set_xticks(np.arange(-5, 6, x_scale))
    ax.set_yticks(np.arange(-5, 6, y_scale))

    # Add grid and labels
    ax.grid()
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)

# Create a NumPy array with vectors (each row is a vector)
vectors = np.array([[2, 5], [1, 2], [1, 1.5], [1, 3], [0, -1], [-1, 1]])

# Create a figure and axis
fig1, ax1 = initialize_plot_window_3d()
fig2, ax2 = initialize_plot_window_3d()



# Mirror 3d
# vectors_3d = np.array([[0, 0, 5], [0, 0, -5], [0,0,3]])
# plot_vectors_3d(vectors_3d, ax1, "Initial Vectors", 1, 1, 1)
# new_vectors = mirror_with_respect_to_XY_plane_3d(vectors_3d)
# print(new_vectors)
# plot_vectors_3d(new_vectors, ax2, "Mirrored Vectors", 1,1, 1)


# Mirrored across X
# plot_vectors(vectors, ax1, "Initial Vectors", 1, 1)
# new_vectors = mirror_with_respect_to_axis_2d(Axis.X_axis, vectors)
# plot_vectors(new_vectors, ax2, "Mirrored Vectors", 1,1)

# ROTATE CLOCKWISE
# plot_vectors(vectors, ax1, "Initial Vectors", 1, 1)
# new_vectors = rotate_2d_counter_clockwise(90, vectors)
# plot_vectors(new_vectors, ax2, "Rotated Vectors", 1,1)

# CHANGE SCALE
# plot_vectors(vectors, ax1, "Initial Vectors", 1, 1)
# new_vectors = change_scale(2, vectors, 2)
# plot_vectors(new_vectors, ax2, "Scaled Vectors", 1,1)



plt.draw()
plt.pause(5)


# Keep the plot open
plt.show()
