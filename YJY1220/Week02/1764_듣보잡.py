# BOJ - 1764.듣보잡
# memory: 43920 KB, times: 2416 ms, lang: python
# 각 집합별 구한 후 교집합 구하기 - 시간 개 오래 걸림;

import sys

N, M = map(int, input().split())
dic = {}

# 듣도 못한 사람
for _ in range(N):
    name = input().strip()
    dic[name] = 1  

# 보도 못한 사람
for _ in range(M):
    name = input().strip()
    if name in dic:
        dic[name] += 1  
    else:
        dic[name] = 1  # 처음이면 1

# 듣도 보도 못한 사람들 교집합 
res = []  
for name, count in dic.items():
    if count == 2:  #둘다 해당 시 
        res.append(name)
res.sort()

print(len(res))
for name in res:
    print(name)
