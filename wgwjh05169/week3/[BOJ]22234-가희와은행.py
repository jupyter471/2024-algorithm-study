# momory: 84176KB, time: 696ms

# N: 시뮬레이션을 시작하는 시점에 대기 큐에 대기 중인 손님 수
# T: 카운터에서 한 번에 작업 가능한 시간
# W: 시뮬레이션을 진행할 시간
# M: 시뮬레이션을 시작한 후에 대기 큐에 입장하는 손님 수
# pi, ti, ci: i번째 손님의 ID, 소요 시간, 입장 시간

# 61% IndexError
# 손님 단위로 시뮬레이션을 수행해 입장하는 손님과 다시 대기 큐에 들어가는 손님의 순서가 올바르지 않게 됨
# -> 1초 단위 시뮬레이션으로 수정

import sys
from collections import deque
import heapq


input = sys.stdin.readline


waiting_queue = deque()     # ID-필요시간 쌍의 큐
N, T, W = map(int, input().split())
for i in range(1, N+1):
    pi, ti = map(int, input().split())
    waiting_queue.append([pi, ti])

admittance_queue = []       # 입장시간-ID-필요시간 쌍의 큐
M = int(input())
for i in range(M):
    pi, ti, ci = map(int, input().split())
    heapq.heappush(admittance_queue, (ci, pi, ti))


now = 0
rest_time = 0
visitor = [0, 0]
head_of_admittance = heapq.heappop(admittance_queue)
while now < W:
    if head_of_admittance and head_of_admittance[0] <= now:
        waiting_queue.append(list(head_of_admittance)[1:])  # 입장시간 정보 제거 후 대기 큐에 추가
        if admittance_queue:
            head_of_admittance = heapq.heappop(admittance_queue)
        else:
            head_of_admittance = None

    if visitor[1] == 0:
        visitor = waiting_queue.popleft()
        rest_time = T

    if rest_time == 0:
        waiting_queue.append(visitor)
        visitor = waiting_queue.popleft()
        rest_time = T

    visitor[1] -= 1
    rest_time -= 1
    print(visitor[0])

    now += 1
