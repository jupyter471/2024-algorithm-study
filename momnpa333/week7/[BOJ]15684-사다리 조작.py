import sys
from itertools import combinations
import copy

input=sys.stdin.readline
N,M,H=map(int,input().split())

board=[[False for _ in range (N+1)] for _ in range (H+1)]

for _ in range(M):
    r,c=map(int,input().split())
    board[r][c]=True

def ispossible(N,H,board,addOn):
    check=[]
    for item in addOn:
        if board[item[0]][item[1]]==True:
            check.append(item)
        board[item[0]][item[1]]=True


    for col in range(1,N+1):
        cur_position=col
        for row in range(1,H+1):
            if board[row][cur_position]==True:
                cur_position+=1
            elif board[row][cur_position-1]==True:
                cur_position-=1
        if cur_position!=col:
            for item in addOn:
                if item not in check:
                    board[item[0]][item[1]]=False
            return False
    for item in addOn:
            if item not in check:
                board[item[0]][item[1]]=False
    return True


ary=[(r,c) for r in range(1,H+1) for c in range(1,N)]


for i in range(4):
    for item in combinations(ary,i):
        if ispossible(N,H,board,item)==True:
            print(i)
            exit(0)
print(-1)
