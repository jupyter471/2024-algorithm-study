# 42204KB, 100ms

import sys


def find():
    i, j = -1, -1
    sum = 0
    length = 100001
    while j < len(numbers) - 1:

        while sum < S and j < len(numbers) - 1:
            j += 1
            sum += numbers[j]

        while sum >= S and i < j:
            if j - i < length:
                length = j - i
            i += 1
            sum -= numbers[i]

    if length == 100001:
        return 0

    return length


N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

print(find())
