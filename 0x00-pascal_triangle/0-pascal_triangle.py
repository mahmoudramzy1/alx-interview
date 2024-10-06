#!/usr/bin/python3
"""making pascal triangle"""


def pascal_triangle(n):
    """function that makes pascal triangle with n of arrays """
    big = []

    if n <= 0:
        return []
    else:
        big = [[1]]

        if n >= 2:
            for i in range(1, n):
                row = [1]
                for j in range(1, i):
                    row.append(big[i-1][j-1] + big[i-1][j])
                row.append(1)
                big.append(row)
    return big
