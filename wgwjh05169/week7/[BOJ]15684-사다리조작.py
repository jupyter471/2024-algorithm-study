# 112196KB, 2208ms

import sys
from itertools import product
from itertools import combinations


def solution():
    for _ in range(M):
        i, j = map(lambda x: int(x)-1, input().split())
        matrix[i][j] = True

    if go():
        return 0

    points = product(range(H), range(N-1))
    for re in range(1, 4):
        for case in combinations(points, re):
            if not connectable(case):
                continue

            for i, j in case:
                matrix[i][j] = True

            if go():
                return len(case)

            for i, j in case:
                matrix[i][j] = False

    return -1


def connectable(case):
    for i, j in case:
        if matrix[i][j]:
            return False

        if j + 1 < N - 1 and matrix[i][j + 1]:
            return False

        if j - 1 >= 0 and matrix[i][j - 1]:
            return False

    return True


def go():
    for root in range(N):
        cj = root
        for ci in range(H):
            if matrix[ci][cj]:
                cj += 1
            elif cj - 1 >= 0 and matrix[ci][cj-1]:
                cj -= 1

        if cj != root:
            return False

    return True


input = sys.stdin.readline
N, M, H = map(int, input().split())
matrix = [[False for j in range(N)] for i in range(H)]
print(solution())
