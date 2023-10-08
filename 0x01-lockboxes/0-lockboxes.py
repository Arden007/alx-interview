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


def canUnlockAll(data):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists where each inner list represents a box containing keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    # number of boxes in the list
    boxes = len(data)
    # to keep track of the boxes visted
    boxes_visted = [False] * boxes
    # the first box is always unlocked
    boxes_visted[0] = True

    # init a stack that will keep track of the box with key in them
    stack = [0]

    while stack:
        # remove and return the current item in the list
        current_box = stack.pop()
        # print(current_box)

        # loop over your data with 
        for key in data[current_box]:
            # if the box not empty shall we allow the stack to continue
            if not boxes_visted[key]:
                # if there is a key in the box set boxes_visted from False to True
                boxes_visted[key] = True
                # add next node or box to be visted
                stack.append(key)
    # finally we check if all the values in boxes_visted is set to True ,since it was init it to false
    return all(boxes_visted)
