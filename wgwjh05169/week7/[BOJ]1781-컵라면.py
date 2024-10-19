# 82716KB 548ms

import sys
import heapq


def solve(N):
    homeworks = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    homeworks.sort(key=lambda x: (x[0], -1 * x[1]))

    done = []
    for hw in homeworks:
        heapq.heappush(done, hw[1])
        if len(done) > hw[0]:
            heapq.heappop(done)

    return sum(done)


print(solve(int(sys.stdin.readline())))
