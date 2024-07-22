# BOJ - 30804.과일탕후루
# Memory : 34808 KB. times: 2032ms, lang : python
# 전체 돌고, 과일종류, 체크리스트 한 후, 집어넣은 큐 방식으로 앞에서부터 뺌 -> 이후 최대 길이 비교 저장해서 출력

# 입력
N = int(input())
fruits = list(map(int, input().split()))

fruit_type = 0
cnt = [0] * 10
max_len = 0
res = []

for i in range(N):
    fruit = fruits[i]
    res.append(fruit) #res에 과일 집어넣기 

    if cnt[fruit] == 0: 
        fruit_type += 1 #체크되어 있지 않은 새로운 과일 종류 추가 
    cnt[fruit] += 1 #해당 과일 종류를 체크했음 

    #과일 종류 2개 초과인 경우 
    while fruit_type > 2: 
        front_fruit = res.pop(0) #앞에서 빼기 
        cnt[front_fruit] -= 1 #체크한 거에서 빼기
        if cnt[front_fruit] == 0:
            fruit_type -= 1 #과일 종류 수 하나 줄이기 

    max_len = max(max_len, len(res))

print(max_len)