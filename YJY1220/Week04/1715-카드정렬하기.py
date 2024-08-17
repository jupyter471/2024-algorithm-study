# 1715 - 카드 정렬하기
# memory: 33972 KB, times: 2504 ms, lang: python3 
# 최소힙으로 가장 작은 값, 두번째 작은 값 -> 총 비교횟수 더하긴

import sys 
import heapq

N = int(sys.stdin.readline())

ansheap = []
res = 0

for i in range(N):
    size = int(input())
    heapq.heappush(ansheap, size)

# 1개인 경우 예외처리 
while(len(ansheap) > 1):
    # 가장 작은거
    data1 = heapq.heappop(ansheap)
    # 두 번째로 작은거
    data2 = heapq.heappop(ansheap)
    cnt = data1 + data2
    res += cnt 
    #합친 값 다시 힙에 넣기 
    heapq.heappush(ansheap, cnt)

print(res)
