# 22234 - 가희와 은행
# memory: , times: , lang: python3 
# 수정중 

import sys 
from collections import deque

input = sys.stdin.readline

N, T, W = map(int, input().split())
queue = deque()

# 영업 전
for _ in range(N):
    p, t = map(int, input().split()) 
    queue.append((p, t))

M = int(input())
customers = []

# 영업 후 
for _ in range(M):
    p, t, c = map(int, input().split())
    customers.append((p, t, c))

# 들어온 시간대로 손님 정렬
customers.sort(key=lambda x: x[2])

# 현재 처리 중
current_customer = 0
current_time = 0
j = 0

# 특정 시간 동안 반복
for i in range(W):
    # 현재 시점에 손님이 들어오는 경우
    while j < len(customers) and customers[j][2] == i + 1:
        queue.append((customers[j][0], customers[j][1]))
        j += 1

    # 현재 손님이 없는 경우 대기열에서 손님을 꺼냄
    if current_customer == 0 and queue:
        current_customer, current_time = queue.popleft()

    if current_customer != 0:
        print(current_customer)  # 현재 손님 출력
        current_time -= 1  # 처리 시간 감소
        # 처리 완료 여부 확인
        if current_time == 0:
            current_customer = 0  # 손님 나감 

        # 업무 시간이 T에 도달 시, 현재 손님을 대기열 맨 뒤로 
        elif current_time > 0 and (W - i - 1) > 0 and i % T == T - 1:
            queue.append((current_customer, current_time))
            #현재 손님 초기화
            current_customer = 0 
    else:
        print(0)  
