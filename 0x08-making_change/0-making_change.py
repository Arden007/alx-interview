#!/usr/bin/python3
"""
Module determines the fewest number of coins needed to meet a given amounttotal
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.

    :param coins: List of coin values
    :type coins: List[int]
    :param total: Total amount to be achieved
    :type total: int
    :return: Fewest number of coins needed to meet total
    :rtype: int
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins, reverse=True)
        counter = 0
        for coin_value in coin:
            while total >= coin_value:
                counter += total // coin_value
                total %= coin_value

        return counter if total == 0 else -1
