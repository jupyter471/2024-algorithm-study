import sys
from itertools import permutations
from collections import deque
input=sys.stdin.readline

N=int(input())

hit_info=[list(map(int,input().split())) for _ in range(N)]

# def play_game(sequence,N):
#     score=0
#     sequence=sequence[0:3]+[0]+sequence[3:]
#     cur_attacker=0
#     for base in range(N):
#         base_status=[]
#         out_count=0
#         while out_count<3:
#             if hit_info[base][sequence[cur_attacker]]==0:
#                 out_count+=1
#                 cur_attacker=(cur_attacker+1)%9
#                 continue
#             runner = [0]*hit_info[base][sequence[cur_attacker]]
#             runner[-1]=1
#             base_status=runner+base_status
#             cur_attacker=(cur_attacker+1)%9
#         score+=sum(base_status[3:])
#         base_status=base_status[:3]
#     return score

def play_game2(sequence,N):
    score=0
    sequence=sequence[0:3]+[0]+sequence[3:]
    cur_attacker=0
    for base in range(N):
        out_count=0
        base_1=0; base_2=0; base_3=0
        while out_count<3:
            if hit_info[base][sequence[cur_attacker]]==0:
                out_count+=1
            elif hit_info[base][sequence[cur_attacker]]==1:
                score+=base_3
                base_1, base_2, base_3 = 1,base_1,base_2
            elif hit_info[base][sequence[cur_attacker]]==2:
                score+=(base_2+base_3)
                base_1,base_2,base_3=0,1,base_1
            elif hit_info[base][sequence[cur_attacker]]==3:
                score+=(base_1+base_2+base_3)
                base_1,base_2,base_3=0,0,1
            elif hit_info[base][sequence[cur_attacker]]==4:
                score+=(1+base_1+base_2+base_3)
                base_1=0; base_2=0; base_3=0
                
            cur_attacker=(cur_attacker+1)%9
    return score


answer=0

# print(play_game2([4,5,6,1,2,3,4,5],N))

for sequence in permutations(range(1,9)):
    score = play_game2(list(sequence),N)
    if answer<score:
        answer=score

print(answer)
