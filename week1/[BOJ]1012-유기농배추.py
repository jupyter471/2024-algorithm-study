import sys
from collections import deque

input = sys.stdin.readline


def test():
    global N, M, field, visited
    N, M, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        field[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                visit_adj_node(i, j)
                cnt += 1

    return cnt


dist = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def visit_adj_node(i, j):
    global N, M, field
    queue = deque()

    field[i][j] = 0
    queue.append((i, j))
    while queue:
        pi, pj = queue.popleft()
        for di, dj in dist:
            ni = pi + di
            nj = pj + dj
            if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == 1:
                field[ni][nj] = 0
                queue.append((ni, nj))


n = int(input())
for _ in range(n):
    print(test())
