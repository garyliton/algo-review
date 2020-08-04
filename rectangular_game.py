# def function(steps, n):
#     x = []
#     y = []
#     for step in steps:
#         a, b = map(int, step.split())
#         x.append(a)
#         y.append(b)
#     return (min(x) * min(y))
#
#     # row_sets = []
#     # col_sets = []
#     # for step in steps:
#     #     row_bound, col_bound = map(int, step.split(' '))
#     #     row_range = list(range(0, row_bound))
#     #     col_range = list(range(0, col_bound))
#     #
#     #     row_sets.append(set(row_range))
#     #     col_sets.append(set(col_range))
#     #
#     # row_intersection = set.intersection(*row_sets)
#     # col_intersection = set.intersection(*col_sets)
#     #
#     # cells = len(row_intersection) * len(col_intersection)
#     #
#     # return cells
#
# print(function(["2 3", "3 7", "4 1"], 3))


# !/bin/python3

import os
import sys


# Complete the solve function below.
def solve(steps):
    x = []
    y = []
    for step in steps:
        print(step)
        a, b = map(int, step.split())
        x.append(a)
        y.append(b)
    return min(x) * min(y)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    steps = []

    for _ in range(n):
        steps.append(list(map(int, input().rstrip().split())))

    result = solve(steps)

    fptr.write(str(result) + '\n')

    fptr.close()
