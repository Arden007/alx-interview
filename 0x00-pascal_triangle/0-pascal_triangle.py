#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]
            current_row = [1]
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])
            current_row.append(1)
            triangle.append(current_row)

    return triangle
