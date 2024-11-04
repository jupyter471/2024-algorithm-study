# LIS DP 풀이
# 31120KB, 36ms

import sys


def solution():

    maximum = -1
    dp = []
    for i, child in enumerate(children):
        dp.append(1)

        for j in range(0, i):
            if child > children[j]:
                dp[i] = dp[j] + 1 if dp[j] + 1 > dp[i] else dp[i]

        if dp[-1] > maximum:
            maximum = dp[-1]

    return N - maximum


N = int(sys.stdin.readline())
children = [int(sys.stdin.readline()) for _ in range(N)]
print(solution())
