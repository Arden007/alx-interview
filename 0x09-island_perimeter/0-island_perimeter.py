#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): A list of lists representing the island.

    Returns:
        int: The perimeter of the island.

    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
