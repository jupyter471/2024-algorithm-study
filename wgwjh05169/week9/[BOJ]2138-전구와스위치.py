import sys


def solution():
    press_case = [(start[0] + 1) % 2] + [(start[1] + 1) % 2] + start[2:]
    unpress_case = start[:]

    pcnt = 1
    ucnt = 0
    for i in range(1, n):
        if press_case[i - 1] != target[i - 1]:
            press_case[i - 1] = (press_case[i - 1] + 1) % 2
            press_case[i] = (press_case[i] + 1) % 2
            if i != n - 1:
                press_case[i + 1] = (press_case[i + 1] + 1) % 2
            pcnt += 1

        if unpress_case[i - 1] != target[i - 1]:
            unpress_case[i - 1] = (unpress_case[i - 1] + 1) % 2
            unpress_case[i] = (unpress_case[i] + 1) % 2
            if i != n - 1:
                unpress_case[i + 1] = (unpress_case[i + 1] + 1) % 2
            ucnt += 1

    if press_case[-1] == target[-1] and unpress_case[-1] == target[-1]:
        return min(pcnt, ucnt)

    if press_case[-1] == target[-1]:
        return pcnt
    if unpress_case[-1] == target[-1]:
        return ucnt

    return -1


n = int(sys.stdin.readline())
start = list(map(int, sys.stdin.readline().rstrip()))
target = list(map(int, sys.stdin.readline().rstrip()))

print(solution())
