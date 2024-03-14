#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """Determine the winner of the game.

    Args:
        x (int): Number of rounds.
        nums (list): List of numbers for each round.

    Returns:
        str or None: Name of the player who won
        the most rounds, or None if winner cannot be determined.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    # Initialize a list to track whether each number is prime
    primes = [1] * (max(nums) + 1)
    primes[0], primes[1] = 0, 0

    # Sieve of Eratosthenes algorithm to mark non-prime numbers
    for i in range(2, len(primes)):
        if primes[i]:
            j = 2
            while i * j < len(primes):
                primes[i * j] = 0
                j += 1

    # Determine the winner for each round based on the sum of prime numbers
    for n in nums:
        if sum(primes[:n + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
