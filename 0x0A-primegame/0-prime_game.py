#!/usr/bin/python3

"""
prime_game.py - Module for implementing the Prime Game.

This module provides functions to play a prime game where Maria and Ben
take turns choosing a prime number from a set of consecutive integers and
removing that number and its multiples. The player who cannot make a move
loses the game.The module includes a function to check if a number is prime
and another function to determine the winner of each round.

Functions:
- is_prime(num): Check if a given number is prime.
- isWinner(x, nums): Determine the winner of each round in the prime game.

Usage:
1. Import the module in your Python script:
   from prime_game import isWinner

2. Use the isWinner function to play the prime game:
   result = isWinner(3, [4, 5, 1])
   print(result)
"""


def is_prime(num):
    """
    Check if a given number is prime.

    Args:
    - num (int): The number to check for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determine the winner of each round in a prime game.

    Args:
    - x (int): The number of rounds to play.
    - nums (List[int]): An array of integers representing the range of
    consecutive integers for each round.

    Returns:
    - str or None: The name of the player with the most wins (Maria or Ben).
    If the winner cannot be determined, return None.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_nos = [i for i in range(1, n + 1) if is_prime(i)]
        if len(prime_nos) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
