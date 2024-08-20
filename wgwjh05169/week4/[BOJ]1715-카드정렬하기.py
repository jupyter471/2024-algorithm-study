# 95% 틀렸습니다.: n이 1인 경우 비교하지 않으니 0 출력 & exit 호출
# 33972KB, 148ms

import sys
import heapq

input = sys.stdin.readline
heap = list()

n = int(input())
for i in range(n):
    heap.append(int(input()))
heapq.heapify(heap)

if n == 1:
    print(0)
    exit(0)

sum = 0
while len(heap) > 1:
    new_cards = heapq.heappop(heap) + heapq.heappop(heap)
    sum += new_cards
    heapq.heappush(heap, new_cards)
print(sum)
