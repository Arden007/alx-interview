#!/usr/bin/python3
"""
Module to rotate a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix (list of lists): The input matrix to be rotated.

    Returns:
    - None: The matrix is edited in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        # Reverse the elements in each row
        matrix[i] = matrix[i][::-1]
