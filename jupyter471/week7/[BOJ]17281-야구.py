"""
브루트포스? 순열 8!
N : 이닝 수
각 선수가 각 이닝에서 얻는 결과가 제공
-> 가장 높은 득점
-> 각 이닝에서 촤대한 많은 선수들이 진루해야함
1번째 순서는 무조건 4번타자
타석 순이랑 타자 순은 구분 잘해야됨
"""
import sys
from itertools import permutations

def game(case,n, result):
    curr_inning = 0
    rotation = case[:3] + [0] + case[3:]
    # print(rotation)
    point = 0
    curr_player = 0   #현재 플레이해야하는 선수에 해당하는 rotaion 내에서의 인덱스 -> rotation[curr_player] 에 해당하는 번호의 선수가 플레이함
    while curr_inning < n:
        #각 이닝 시작
        out_count = 0
        b1 = b2 = b3 = 0  #각 베이스에 와있는 선수
        #플레이 시작
        while out_count < 3:   #이전 이닝에서 끝난 이후부터 다시 시작해야됨
            if result[curr_inning][rotation[curr_player]] == 0:
                #out
                out_count += 1
            elif result[curr_inning][rotation[curr_player]] == 1:
                point += b3  # b3에 진루했던 선수가 있다면 득점
                b1,b2,b3 = 1,b1,b2   #진루
            elif result[curr_inning][rotation[curr_player]] == 2:
                point += b2 + b3
                b1,b2,b3 = 0,1,b1
            elif result[curr_inning][rotation[curr_player]] == 3:
                point += b1+b2+b3
                b1,b2,b3 = 0,0,1  #모두 다 홈인하고 3루에만 선수 있음
            else:
                #홈런
                point += (b1+b2+b3+1)
                b1,b2,b3 = 0,0,0  #모든 베이스는 비게된다
            curr_player += 1
            if curr_player == 9:  #한바퀴 다 돌았으면 다시 처음부터
                curr_player = 0
        curr_inning += 1
    return point

N = int(input())
result = [] #각 선수가 각 이닝에서 얻는 결과 1번 선수 ~ 9번 선수
player = [i for i in range(1,9)]

for _ in range(N):
    result.append(list(map(int,sys.stdin.readline().split())))

#모든 경우의 수 단 여기에 1번선수는 빠져 있음
cases = list(permutations(player))
score = 0
for case in cases:
    score = max(score, game(list(case),N,result))
print(score)
