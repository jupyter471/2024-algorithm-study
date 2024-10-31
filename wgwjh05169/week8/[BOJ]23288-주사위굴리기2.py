# 31120KB, 480ms

import sys


BOTTOM = 5
DIR_SIZE = 4
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def move(si, sj, idx):
    global score

    i, j, idx = move_dice(si, sj, idx)
    roll_dice(idx)

    score += count_same_movable(i, j) * board[i][j]

    if dice[BOTTOM] > board[i][j]:
        idx = (idx + 1) % DIR_SIZE
    elif dice[BOTTOM] < board[i][j]:
        idx = (idx - 1) % DIR_SIZE

    return i, j, idx


def move_dice(si, sj, idx):
    i = si + directions[idx][0]
    j = sj + directions[idx][1]
    if not (0 <= i < N and 0 <= j < M):
        idx = (idx + 2) % DIR_SIZE
        i = si + directions[idx][0]
        j = sj + directions[idx][1]

    return i, j, idx


def roll_dice(idx):
    global dice

    if idx == 0:
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
        return
    if idx == 2:
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
        return
    if idx == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
        return
    if idx == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
        return


def count_same_movable(si, sj):
    count = 0
    stack = [(si, sj)]
    visited = set()
    visited.add((si, sj))
    value = board[si][sj]
    while stack:
        i, j = stack.pop()
        count += 1
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited and board[ni][nj] == value:
                stack.append((ni, nj))
                visited.add((ni, nj))

    return count


N, M, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dice = [2, 4, 1, 3, 5, 6]
score = 0
i, j, idx = 0, 0, 0
for _ in range(K):
    i, j, idx = move(i, j, idx)

print(score)
