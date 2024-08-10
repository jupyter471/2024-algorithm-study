"""
n개의 과일
과일 종류 1-9
-> 두종류 이하로 사용하여 탕후루 만들기
앞 뒤로 빼기
"""
from collections import defaultdict
n = int(input())
tang = list(map(int, input().split()))

tang_set = set(tang)
type_num = len(tang_set)
if type_num <= 2:
    print(n)
    exit(0)  #0으로 안하면 백준에서 런타임에러 뜸

fruit_count = defaultdict(int)
start = 0
end = 0
answer = 0 #최대길이
cnt = 0
while end < n:
    if fruit_count[tang[end]] == 0:  #나온 적 없음
        cnt += 1
    fruit_count[tang[end]] += 1
    while cnt > 2:
        #start 옮기기
        fruit_count[tang[start]] -= 1
        if fruit_count[tang[start]] == 0:
            cnt -= 1  #과일 제거 완료
        start += 1
    end += 1
    answer = max(answer, end - start)

print(answer)
"""
투포인터
과일의 종류가 2개뿐인 구간의 길이 구하기
end과일이 기존 과일 2개와 다르다면 -> start += 1
end과일이 기존 과일 2개 이하 -> end += 1

-> 중간중간 최대 길이 갱신해야함
"""