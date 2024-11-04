#100번 칸을 넘어간다면 이동할 수 없다. 
#도착한 칸이 사다리면, 사다리를 타고 위로 올라간다. 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다.
#1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다. 항상 100번 칸에 도착할 수 있는 입력만 주어진다.

import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
bridge=dict()
for _ in range(N+M):
    u,v=map(int,input().split())
    bridge[u]=v

dq=deque([])
position=1
check={1,}

dq.append(1)

count=0

while dq:
    count+=1
    for _ in range(len(dq)):
        pos=dq.popleft()
        for i in range(1,7):
            next=pos+i
            if next in bridge:
                next=bridge[next]
            if next==100:
                print(count)
                exit(0)
            if next<=100 and next not in check:
                dq.append(next)
                check.add(next)


