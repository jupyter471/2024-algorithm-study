# 238972KB, 2056ms

import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)


def clean(curr):
    global children

    for child in children[curr]:
        children[child].remove(curr)
        clean(child)


def flow(curr, given):
    global children, water

    if not children[curr]:
        water[curr] = given
        return

    for child in children[curr]:
        flow(child, given / len(children[curr]))


def solution():
    global children, water

    N, W = map(int, sys.stdin.readline().split())
    children = defaultdict(list)
    water = defaultdict(int)
    for _ in range(N-1):
        u, v, = map(int, sys.stdin.readline().split())
        children[u].append(v)
        children[v].append(u)

    clean(1)

    flow(1, W)

    return sum(water.values()) / len(water)


print(solution())
