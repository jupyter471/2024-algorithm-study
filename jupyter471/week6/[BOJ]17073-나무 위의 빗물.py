"""
근데 결국엔 루트에만 물이 있을 거 아님? -> 리프 노드의 개수를 구하면 되는 문제
"""

from collections import defaultdict
root = 1

tree = defaultdict(list)

n, w = map(int, input().split())
for _ in range(n-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)  #양방향으로 저장

leaf_count = 0

for node in range(2,n+1):  #루트 다음 노드부터 탐색
    if len(tree[node]) == 1:
        leaf_count += 1

print(w/leaf_count)
