# 35560KB, 60ms

import sys
from collections import deque
import heapq

input = sys.stdin.readline


def find_eatable():
    queue = deque()
    queue.append((bi, bj))
    visited = set()
    visited.add((bi, bj))
    dist = 1

    while queue:
        cnt = len(queue)
        for _ in range(cnt):
            ci, cj = queue.popleft()

            for di, dj in direct:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
                    if matrix[ni][nj] == 0 or matrix[ni][nj] == bsize:
                        queue.append((ni, nj))
                        visited.add((ni, nj))
                        continue

                    if matrix[ni][nj] < bsize:
                        heapq.heappush(eadtable, (ni, nj))

        if eadtable:
            break

        dist += 1

    return dist


direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
    if 9 in matrix[-1]:
        bi = i
        bj = matrix[-1].index(9)
        matrix[bi][bj] = 0
bsize = 2

ans = 0
cnt = 0
while True:
    eadtable = []
    dist = find_eatable()

    if len(eadtable) == 0:
        break

    ans += dist
    bi, bj = heapq.heappop(eadtable)
    matrix[bi][bj] = 0
    cnt += 1
    if cnt == bsize:
        cnt = 0
        bsize += 1

print(ans)
