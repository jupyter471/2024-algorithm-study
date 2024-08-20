"""
N개의 문제는 모두 풀어야 한다.
먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
가능하면 쉬운 문제부터 풀어야 한다.
n: 문제 개수 m : 먼저 문제 정보 개수
A B : A 문제가 B보다 먼저

위상정렬
"""
import heapq
from collections import defaultdict
n,m = map(int, input().split())
graph = defaultdict(list)
indegree = [0] * (n+1)
pq = []
result = []
for _ in range(m):
    a,b = map(int, input().split())   #a->b
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        #차수 0인 노드
        heapq.heappush(pq, i)
    while pq:
        nxt = heapq.heappop(pq)
        result.append(nxt)
        for x in graph[nxt]:
            indegree[x] -= 1
            if indegree[x] == 0:
                heapq.heappush(pq, x)

print(*result, sep=" ")