# 31120KB, 44ms

import sys


def can_cross(road: list, ramp: list):
    flat_start = 0
    for i in range(N-1):
        gap = road[i] - road[i+1]
        if gap == 0:
            continue

        if abs(gap) > 1:
            return False

        if gap < 0:
            if i - flat_start < L - 1:
                return False
            for di in range(0, L):
                if ramp[i - di]:
                    return False
                ramp[i - di] = True
            flat_start = i + 1
        else:
            flat_start = i + 1

    return True


N, L = map(int, sys.stdin.readline().split())
roadmap = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
cnt = 0
for i in range(N):
    ramp = [False for _ in range(N)]
    if can_cross(roadmap[i], ramp) and can_cross(roadmap[i][::-1], ramp[::-1]):
        cnt += 1

roadmap = list(zip(*roadmap))
for i in range(N):
    ramp = [False for _ in range(N)]
    if can_cross(roadmap[i], ramp) and can_cross(roadmap[i][::-1], ramp[::-1]):
        cnt += 1

print(cnt)
