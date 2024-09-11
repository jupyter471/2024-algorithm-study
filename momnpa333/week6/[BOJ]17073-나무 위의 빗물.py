# 리프 노드수 / 전체 빗물의 양

import sys
from collections import deque

input = sys.stdin.readline

N,rain = map(int,input().split(" "))

tree = [[] for _ in range(N+1)]

def cal_leaf_num(N):
    leaf_num=0

    check=[False for _ in range(N+1)]

    dq=deque([])

    dq.append(1)

    while dq:
        parent=dq.popleft()
        check[parent]=True
        for child in tree[parent]:
            if len(tree[child])==1 and check[child]==False:
                leaf_num+=1
            else:
                if check[child]==False:
                    dq.append(child)
    return leaf_num

def cal_leaf_num2(N):
    leaf_num=0
    for node in tree[2:]:
        if len(node) == 1:
            leaf_num += 1
    return leaf_num

for i in range(N-1):
    U,V= map(int,input().split())
    tree[U].append(V)
    tree[V].append(U)


leaf_num=cal_leaf_num2(N)

print(rain/leaf_num)

