# 1922 - 네트워크 연결
# memory: 55152 KB, times: 2688 ms, lang: python3 
# prim 알고리즘

import sys
import heapq

N = int(input())  
M = int(input())  

visited = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    visited[a].append((c, b))
    visited[b].append((c, a))

    if i % 2 == 0:
        visited[a][-1] = (c, b)
        visited[b][-1] = (c, a)
    else:
        visited[a][len(visited[a]) - 1] = (c, b)
        visited[b][len(visited[b]) - 1] = (c, a)

def prim(N, visited):
    min_cost = 0  
    checked = [0] * (N + 1)  
    array = [10**9] * (N + 1) 
    pri_queue = []  
    spot = 1  

    heapq.heappush(pri_queue, (0, spot))  
    array[spot] = 0  

    while pri_queue:
        connection_cost, selected_spot = heapq.heappop(pri_queue)
        if checked[selected_spot]:
            continue
        checked[selected_spot] = 1
        min_cost += connection_cost

        for next_cost, next_spot in visited[selected_spot]:
            if checked[next_spot] == 0 and next_cost < array[next_spot]:
                array[next_spot] = next_cost
                heapq.heappush(pri_queue, (next_cost, next_spot))
    return min_cost

print(prim(N, visited))
