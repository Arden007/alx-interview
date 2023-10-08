#!/usr/bin/python3

"""
Module: lockboxes.py

This module provides a function for determining whether all the boxes in a sequence
of locked boxes can be opened. Each box may contain keys to other boxes, and the goal
is to check if all boxes can be unlocked starting from the first box.

Example Usage:
    from lockboxes import canUnlockAll

    boxes = [[1], [2], [3], [4], []]
    result = canUnlockAll(boxes)
    print(result)  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    result = canUnlockAll(boxes)
    print(result)  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    result = canUnlockAll(boxes)
    print(result)  # False
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists where each inner list represents a box containing keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    # Number of boxes in the list
    num_boxes = len(boxes)
    # To keep track of the boxes visited
    visited = [False] * num_boxes
    # The first box is always unlocked
    visited[0] = True

    # Initialize a stack that will keep track of the boxes with keys in them
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Loop over the keys in the current box
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    # Finally, check if all the values in 'visited' are True (all boxes were visited)
    return all(visited)
