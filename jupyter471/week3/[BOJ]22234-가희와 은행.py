"""
N, T, W 입력
두 번째 줄 부터 N개의 줄에는 0초일 때, 대기 큐의 앞에 있는 고객부터, Px와 고객이 일을 처리하는 데 필요한 시간 tx가 공백으로 구분되어 주어집니다.
N+2번째 줄에는, 1초 이후에 은행에 들어온 고객 수 M이 주어집니다.

N+3번째 줄부터 M개의 줄에 걸쳐서, Px, tx, cx가 공백으로 구분되어 주어집니다. 입력된 순서대로 각각 N+1, ..., N+M번 고객입니다.

N+1 손님 -> C_(N+1)초 후 들어옴

큐써야됨
"""

# 메모리: 182396 KB, 시간: 760 ms

import sys
from collections import deque
N,T,W = map(int, input().split())
waiting = deque()
for _ in range(N):
    waiting.append(list(map(int,sys.stdin.readline().split())))  #대기 큐 고객 -> id,소요시간

after = []
M = int(input()) #1초
for _ in range(M):
    after.append(list(map(int, sys.stdin.readline().split())))  #id,소요시간,오픈 후 흐른 시간
after.sort(key=lambda x: x[2]) #입장한 시간순으로 정렬
after = deque(after)

sec = 0 #흐르는 시간

while sec < W:
    now_id, now_t = waiting.popleft()   #id, 소요시간
    if now_t <= T:
        #소요시간이 기준시간보다 작은 경우
        for _ in range(now_t):
            print(now_id)
            sec += 1
            if sec == W:
                exit(0)
        while after and after[0][2] <= sec:
            m = after.popleft()
            waiting.append([m[0], m[1]])
    else:
        for _ in range(T):
            print(now_id)
            sec += 1
            if sec == W:
                exit(0)
        # 대기열 갱신
        while after and after[0][2] <= sec:
            m = after.popleft()
            waiting.append([m[0], m[1]])
        waiting.append([now_id, now_t - T])

#초마다 고객 아이디 출력
#t와 T 비교 후 연산
#할 때마다 after의 c 시간 비교해서 큐에 삽입하기