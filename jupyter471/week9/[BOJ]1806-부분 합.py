"""
길이 N인 수열
합이 S 이상의 최소 길이
못 만들면 0
10 15
5 5 5 10 6 7 5 1 9 10
10 15
5 5 5 10 1 2 3 4 5 9
"""

n,target = map(int, input().split())
num = list(map(int,input().split()))

start = end = 0
number = num[0]
length = float('inf')

while start <= end and end < n:
    if number < target:
        end += 1
        if end < n:
            number += num[end]
    elif number >= target:
        length = min(length, end - start + 1)
        number -= num[start]
        start += 1


if length == float('inf'):
    print(0)
else:
    print(length)
