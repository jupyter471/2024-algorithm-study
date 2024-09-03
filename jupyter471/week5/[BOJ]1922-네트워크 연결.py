"""
최소비용 트리

"""
from collections import defaultdict
import heapq


def minimum_path(graph, v, visited, n):
    pq = []
    visited[v] = True
    cost = 0
    cnt = 1

    for w in graph[v]:
        heapq.heappush(pq, (w[1], w[0]))

    while pq and cnt <= n:
        c, w = heapq.heappop(pq)
        if not visited[w]:
            visited[w] = True
            cost += c
            cnt += 1
            for nxt in graph[w]:
                heapq.heappush(pq, (nxt[1], nxt[0]))
    return cost
def main():
    n = int(input())
    m = int(input())

    graph = defaultdict(list)
    visited = [False] * (n+1)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    cost = minimum_path(graph,1, visited, n)
    print(cost)

main()





