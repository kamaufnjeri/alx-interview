#!/usr/bin/python3
"""
Defines a function makeChange to solve the coin change problem.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the given amount total.

    Args:
        coins (list): List of coin denominations.
        total (int): Target amount to make up using coins.

    Returns:
        int: Fewest number of coins needed to meet total.
             Returns -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output should be 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output should be -1
