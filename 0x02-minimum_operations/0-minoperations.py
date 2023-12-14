#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    def dfs(current, steps):
        if current == 1:
            return steps
        result = float('inf')
        for i in range(1, current):
            if current % i == 0:
                result = min(result, dfs(current // i, steps + i))
        return result

    return dfs(n, 0)
