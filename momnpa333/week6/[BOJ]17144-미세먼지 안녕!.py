import sys
input=sys.stdin.readline

R,C,T=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(R)]

cleaner_index=[]

def spread(board):
    after_board=[[0]*C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if board[r][c]<=0:
                after_board[r][c]+=board[r][c]
                continue
            add_dust=board[r][c]//5
            for add_r,add_c in ((0,1),(1,0),(0,-1),(-1,0)):
                new_r=r+add_r; new_c=c+add_c
                if 0<=new_r<R and 0<=new_c<C and board[new_r][new_c]!=-1:
                    after_board[new_r][new_c]+=add_dust
                    board[r][c]-=add_dust
            after_board[r][c]+=board[r][c]

    return after_board
    

def rotate(board):
    rotate_board=board
    
    # 위쪽 순환
    for idx,dust in enumerate(list(zip(*board))[0][:cleaner_index[0]]):
        rotate_board[idx+1][0]=dust
    
    for idx,dust in enumerate(board[0][1:]):
        rotate_board[0][idx]=dust
    
    for idx,dust in enumerate(list(zip(*board))[C-1][1:cleaner_index[0]+1]):
        rotate_board[idx][C-1]=dust

    for idx,dust in enumerate(board[cleaner_index[0]][1:C-1]):
        rotate_board[cleaner_index[0]][idx+2]=dust

    rotate_board[cleaner_index[0]][1]=0

    ##아래쪽 순환
    for idx,dust in zip(range(cleaner_index[1]+1,R),list(zip(*board))[0][cleaner_index[1]+1:]):
        rotate_board[idx-1][0]=dust
    
    for idx,dust in enumerate(board[R-1][1:]):
        rotate_board[R-1][idx]=dust
    
    for idx,dust in zip(range(cleaner_index[1],R-1),list(zip(*board))[C-1][cleaner_index[1]:R-1]):
        rotate_board[idx+1][C-1]=dust

    for idx,dust in enumerate(board[cleaner_index[1]][1:C-1]):
        rotate_board[cleaner_index[1]][idx+2]=dust

    rotate_board[cleaner_index[1]][1]=0

    rotate_board[cleaner_index[0]][0]=-1; rotate_board[cleaner_index[1]][0]=-1



    return rotate_board
    

def find_cleaner():
    for idx,item in enumerate(list(zip(*board))[0]):
        if item==-1:
            cleaner_index.append(idx)


def solve(board):
    answer=0
    find_cleaner()

    for _ in range(T):
        board=spread(board)
        board=rotate(board)

    for row in board:
        answer+=sum(row)

    return answer+2



print(solve(board))
