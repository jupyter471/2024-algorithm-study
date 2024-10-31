# 111348KB, 980ms

import sys
from itertools import permutations


def solution():
    ans = 0
    for case in map(list, permutations(range(1, 9))):
        score = play(case[:3] + [0] + case[3:])
        if score > ans:
            ans = score

    return ans


def play(players):
    pi, score = 0, 0
    for inning in innings:
        out, first, second, third = 0, 0, 0, 0

        while out < 3:
            player = players[pi]

            if inning[player] == 0:
                out += 1
            else:
                first, second, third, score = advance(inning[player], first, second, third, score)

            pi = (pi + 1) % 9

    return score


def advance(value, first, second, third, score):

    if value == 1:
        score += third
        third, second, first = second, first, 1
    elif value == 2:
        score += third + second
        third, second, first = first, 1, 0
    elif value == 3:
        score += third + second + first
        third, second, first = 1, 0, 0
    elif value == 4:
        score += third + second + first + 1
        third, second, first = 0, 0, 0

    return first, second, third, score


N = int(sys.stdin.readline())
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solution())
