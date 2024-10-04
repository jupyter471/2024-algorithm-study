# 31120KB, 2396ms

import sys


def distribute():
    for i in range(R):
        for j in range(C):
            if room[i][j][0] > 0:
                dust = room[i][j][0]
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and (nj != 0 or ni not in cleaner):
                        room[ni][nj][1] += dust // 5
                        room[i][j][0] -= dust // 5

    for i in range(R):
        for j in range(C):
            room[i][j][0] += room[i][j][1]
            room[i][j][1] = 0

def clean():
    upper_prev = 0
    lower_prev = 0
    # j 이동, i = cleaner
    for j in range(1, C):
        room[cleaner[0]][j][0], upper_prev = upper_prev, room[cleaner[0]][j][0]
        room[cleaner[1]][j][0], lower_prev = lower_prev, room[cleaner[1]][j][0]

    # i 이동, j = C-1
    for i in range(cleaner[0]-1, -1, -1):
        room[i][C-1][0], upper_prev = upper_prev, room[i][C-1][0]
    for i in range(cleaner[1]+1, R):
        room[i][C-1][0], lower_prev = lower_prev, room[i][C-1][0]

    # j 이동, i = 0/R
    for j in range(C-2, -1, -1):
        room[0][j][0], upper_prev = upper_prev, room[0][j][0]
        room[R-1][j][0], lower_prev = lower_prev, room[R-1][j][0]

    # i 이동, j = 0
    for i in range(1, cleaner[0]):
        room[i][0][0], upper_prev = upper_prev, room[i][0][0]
    for i in range(R-2, cleaner[1], -1):
        room[i][0][0], lower_prev = lower_prev, room[i][0][0]


R, C, T = map(int, sys.stdin.readline().split())
room = []
for i in range(R):
    row = sys.stdin.readline()
    if row.startswith('-'):
        cleaner = (i-1, i)
    room.append(list(map(lambda x: [x, 0], map(int, row.split()))))

for t in range(T):
    distribute()
    clean()

ans = 2
for row in room:
    ans += sum(map(lambda x: x[0], row))

print(ans)
