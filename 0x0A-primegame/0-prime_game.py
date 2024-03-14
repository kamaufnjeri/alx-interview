#!/usr/bin/python3
"""Winner from choosing prime numbers"""


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of consecutive
    integers starting from 1 up to and including n, they take turns
    choosing a prime number from the set and removing that number
    and its multiples from the set.
    The player that cannot make a move loses the game.
    """
    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for n in nums:
        # Simulate the game for the current round
        winner = simulate_game(n)

        # Update wins based on the winner of the current round
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return 'Ben'
    else:
        return None


def simulate_game(n):
    # Initialize a list to track removed numbers
    removed = [False] * (n + 1)
    # Sieve of Eratosthenes algorithm to mark non-prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if not removed[i]:
            for j in range(i * i, n + 1, i):
                removed[j] = True

    # Determine the winner based on remaining numbers
    # Maria starts, so if there's a prime number
    # left, Maria wins; otherwise, Ben wins
    if any(not removed[i] for i in range(2, n + 1)):
        return 'Maria'
    else:
        return 'Ben'
