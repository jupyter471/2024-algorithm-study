# 48308KB, 296ms

import sys
import heapq

input = sys.stdin.readline


def mst():
    answer = 0
    while edges:
        w, u, v = heapq.heappop(edges)
        if find(u) == find(v):
            continue

        union(u, v)
        answer += w

    return answer


def union(u, v):
    root = find(u)
    index[root] = find(v)


def find(node):
    while index[node] != node:
        prev = node
        node = index[node]
        index[prev] = index[node]

    return node


N = int(input())
M = int(input())
index = [i for i in range(0, N)]
backup = [i for i in range(0, N)]
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())

    u -= 1
    v -= 1

    heapq.heappush(edges, (w, u, v))

print(mst())
