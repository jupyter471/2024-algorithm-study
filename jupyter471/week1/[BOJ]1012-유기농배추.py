import sys
from collections import deque

#상하좌우 컨드롤러
row_move = [-1,1,0,0]
col_move = [0,0,-1,1]

def bfs():
    cnt = 0
    while q:
        r,c = q.popleft()
        if mat[r][c] == 1:
            q_bfs.append((r,c))
            while q_bfs :
                r,c = q_bfs.popleft()   #배추가 있는 위치, 탐색을 시작할 위치
                for i in range(4):
                    d_row = r + row_move[i]
                    d_col = c + col_move[i]

                    if 0<= d_row < n and 0<= d_col < m and mat[d_row][d_col] == 1:
                        q_bfs.append((d_row,d_col))
                        mat[d_row][d_col] = 0
            cnt = cnt + 1
    return cnt

T = int(input()) #테스트 케이스 개수
for _ in range(T):
    m,n,k = map(int,input().split())
    q = deque()
    q_bfs = deque()
    mat = [[0] * m for _ in range(n)]
    for _ in range(k): #배추 위치 입력
        col,row = map(int,sys.stdin.readline().split())
        mat[row][col] = 1 #배추가 있으면 1
        q.append((row,col)) #배추가 있는 칸 deque에 넣기
    res = bfs()
    print(res)