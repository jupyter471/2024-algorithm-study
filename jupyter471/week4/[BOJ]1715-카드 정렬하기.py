import heapq


# 그리디 -> 현재 비교 횟수가 가장 적은 카드 선택

def main():
    heap = []
    n = int(input())
    for _ in range(n):
        heapq.heappush(heap, int(input()))

    total_sort = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        total_sort += a+b
        heapq.heappush(heap, a+b)

    print(total_sort)

main()