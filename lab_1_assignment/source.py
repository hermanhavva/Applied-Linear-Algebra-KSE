import numpy as np
import math as m
from enum import Enum


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

    for row in range(dimension):
        for column in range(dimension):
            scale_matrix[row][column] = coefficient

    result = []

    for vector in my_object:
        result.append(np.dot(scale_matrix, vector))

    return np.array(result)


def rotate_2d(degree, my_object) -> np.array:
    rotation_matrix_2d = np.array([[m.cos(degree), -m.sin(degree)],
                                   [m.sin(degree), m.cos(degree)]])
    result = []
    for vector in my_object:
        result.append(np.dot(rotation_matrix_2d, vector))

    return np.array(result)


class Axis(Enum):
    X_axis = 1
    Y_axis = 2
    Z_axis = 3


my_axis = Axis.X_axis

myObject = np.array([[1, 2], [0, 1], [1.5, 0]])

print(rotate_2d(45, myObject))
