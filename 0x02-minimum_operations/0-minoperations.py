#!/usr/bin/python3

"""
This module provides a function for calculating the fewest number of operations
needed to achieve a specified number of 'H' characters in a text file using two
operations: Copy All and Paste.

Usage:
    - minOperations(n): Calculate the minimum number of operations needed to
      reach 'n' 'H' characters in the file.

Returns:
    int: The minimum number of operations needed to reach 'n' 'H' characters.
    If it's impossible to achieve 'n', it returns 0.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve exactly 'n'
    H characters in the file.

    Args:
    n (int): The target number of H characters.

    Returns:
    int: The minimum number of operations needed to reach 'n' H characters.
    If it's impossible to achieve, return 0.
    """

    if n <= 1:
        return 0

    operations = 0
    current = 1
    clipboard = 0

    while current < n:
        if n % current == 0:
            clipboard = current
            operations += 2
        else:
            operations += 1

        current += clipboard

    return operations
