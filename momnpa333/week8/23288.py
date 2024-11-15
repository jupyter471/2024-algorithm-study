import sys
from collections import deque
input=sys.stdin.readline

N,M,K=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]

diceRow=[2,1,5,6]
diceCol=[4,1,3,6]

dir_dict={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}

def move_dice(op):
    global diceCol
    global diceRow

    if op==0:
        diceCol=[diceCol[-1]]+diceCol[:3]
        diceRow[-1]=diceCol[-1];diceRow[1]=diceCol[1]
    elif op==1:
        diceRow=[diceRow[-1]]+diceRow[:3]
        diceCol[-1]=diceRow[-1];diceCol[1]=diceRow[1]
    elif op==2:
        diceCol=diceCol[1:]+[diceCol[0]]
        diceRow[-1]=diceCol[-1];diceRow[1]=diceCol[1]
    elif op==3:
        diceRow=diceRow[1:]+[diceRow[0]]
        diceCol[-1]=diceRow[-1];diceCol[1]=diceRow[1]

def make_score_board(board):
    scored_board=[[-1]*M for _ in range(N)]
    dq=deque([])


    for r in range(N):
        for c in range(M):
            fill_position=[]
            if scored_board[r][c]==-1:
                fill_position.append((r,c))
                dq.appendleft((r,c,board[r][c]))
                scored_board[r][c]=0
                cnt=1
                while dq:
                    for _ in range(len(dq)):
                        curR,curC,score=dq.popleft()
                        for addR,addC in ((0,1),(1,0),(0,-1),(-1,0)):
                            R=curR+addR;C=curC+addC
                            if 0<=R<N and 0<=C<M and scored_board[R][C]==-1 and board[R][C]==score:
                                fill_position.append((R,C))
                                cnt+=1
                                scored_board[R][C]=0
                                dq.appendleft((R,C,score))
                for item in fill_position:
                    row,col=item
                    scored_board[row][col]=cnt
    return scored_board

scored_board=make_score_board(board)

position_r=0;position_c=0
answer=0

def play_game(r,c,dir):
    R=r+dir_dict[dir][0];C=c+dir_dict[dir][1]
    if not (0<=R<N and 0<=C<M):
        R=r+dir_dict[dir][0]*-1;C=c+dir_dict[dir][1]*-1
        dir=(dir+2)%4
    move_dice(dir)
    score=board[R][C]*scored_board[R][C] 
    if diceRow[3]>board[R][C]:
        dir=(dir+1)%4
    elif diceRow[3]<board[R][C]:
        dir=(dir-1)%4

    return (R,C,dir,score)

position_r,position_c,dir,score=play_game(0,0,0)
answer+=score

for _ in range(K-1):
    position_r,position_c,dir,score=play_game(position_r,position_c,dir)
    answer+=score
print(answer)


