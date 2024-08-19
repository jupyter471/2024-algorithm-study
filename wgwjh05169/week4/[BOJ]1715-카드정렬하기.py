# 95% 틀렸습니다.

import sys
import heapq

input = sys.stdin.readline
heap = list()

n = int(input())
for i in range(n):
    heap.append(int(input()))
heapq.heapify(heap)

if n == 1:
    print(heap[0])

sum = 0
while len(heap) > 1:
    new_cards = heapq.heappop(heap) + heapq.heappop(heap)
    sum += new_cards
    heapq.heappush(heap, new_cards)
print(sum)
