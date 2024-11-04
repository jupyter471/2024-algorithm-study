# 34052KB, 60ms

import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append((1, 0))
    visited = {1}
    while queue:
        x, count = queue.popleft()

        for dx in range(1, 7):
            nx = x + dx

            if nx == 100:
                return count + 1

            if nx < 100 and nx not in visited:
                queue.append((matrix[x + dx], count + 1))
                visited.add(x + dx)


N, M = map(int, sys.stdin.readline().split())
matrix = [i for i in range(101)]
for _ in range(N + M):
    i, j = map(int, sys.stdin.readline().split())
    matrix[i] = j

print(bfs())
