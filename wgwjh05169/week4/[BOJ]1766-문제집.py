# 41908KB, 172ms

import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for _ in range(N)]
in_degree = [0] * N
for _ in range(M):
    i, j = map(int, input().split())
    adj_list[i-1].append(j-1)
    in_degree[j-1] += 1

# BFS와 Heap을 활용한 위상 정렬
heap = []
result = []
for idx, in_d in enumerate(in_degree):
    if in_d == 0:
        heapq.heappush(heap, idx)

while heap:
    curr = heapq.heappop(heap)
    result.append(curr + 1)

    for next in adj_list[curr]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            heapq.heappush(heap, next)

print(*result, sep=" ")
