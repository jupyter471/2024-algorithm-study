import sys
from collections import Counter

input = sys.stdin.readline


def find_max_count():
    N = int(input())
    tanghuru = list(map(int, input().split()))
    if N < 3:
        return N

    i, j = 0, 1
    max = 2
    types = set()
    types.add(tanghuru[0])
    types.add(tanghuru[1])
    counter = Counter()
    counter[tanghuru[0]] += 1
    counter[tanghuru[1]] += 1
    while j < N - 1:
        if len(types) <= 2:
            j += 1
            counter[tanghuru[j]] += 1
            types.add(tanghuru[j])
        else:
            counter[tanghuru[i]] -= 1
            if counter[tanghuru[i]] == 0:
                types.remove(tanghuru[i])
            i += 1

        if len(types) <= 2 and max < j - i + 1:
            max = j - i + 1

    return max


print(find_max_count())
