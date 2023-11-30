#!/usr/bin/python3
"""
return an empty list if n <= 0
an empty list to append the lists
loop from range 1 to n
create two lists. one for the loop and the other with final results
first list will be [1]
the next will be [0, 1, 0]
create a new loop from 1 to len next list - 1.
we use the second list to add the two items together
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    pascal_list = [[1]]
    temp = [0, 1, 0]

    for i in range(1, n):
        pascal = [1]

        if i > 0:
            for j in range(1, len(temp) - 1):  # Adjust loop range
                pascal.append(temp[j] + temp[j + 1])

        temp = [0] + pascal + [0]

        pascal_list.append(pascal)

    return pascal_list
