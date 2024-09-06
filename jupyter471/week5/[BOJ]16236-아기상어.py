"""
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
처음 아기 상어는 크기가 2
"""
import sys
from collections import deque
n = int(input())  #N x N
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cc = 0
cr = 0
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            cr = i
            cc = j
            sea[i][j] = 0
            break
#상하좌우
dc = [0,0,-1,1]
dr = [-1,1,0,0]

#처음에는 가능한 좌표 다 넣고 pq로 하려했으나 그렇게 하면 조건 만족이 어렵
#bfs로 거리별로 반복문 돌려서 먹을 수 있는게 있다면 stop

def eat_fish(r,c,size):
    q = deque()
    dist = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    q.append((r,c)) #현재 위치 삽입
    visited[r][c]
    fish = []
    while q:
        r,c = q.popleft()
        for i in range(4):
            #상하좌우 이동
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0<= new_r<n and 0<= new_c < n and not visited[new_r][new_c]:
                if sea[new_r][new_c] <= size:
                    #지나갈 수 있는 경우 (자기크기 이하)
                    q.append((new_r, new_c))
                    visited[new_r][new_c] = True
                    dist[new_r][new_c] = dist[r][c] + 1
                    if 0 < sea[new_r][new_c] < size :
                        fish.append((new_r, new_c,dist[new_r][new_c]))
    return sorted(fish, key=lambda x: (-x[2],-x[0],-x[1]))     #가장 위, 가장 왼쪽 순으로 내림차순 정렬

size = 2
time = 0 #잡아먹을 수 있는 시간 (움직인 거리)
cnt = 0 #먹은 개수
while True:
    res = eat_fish(cr,cc,size)
    # print(res)
    if len(res) == 0:
        break #더 이상 먹을 수 있는 것이 없음

    nr, nc, dist = res.pop()  #내림차순 정렬인 상태
    # print(nr, nc, dist)
    time += dist
    sea[nr][nc], sea[cr][cc] = 0,0
    cr, cc = nr, nc
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(time)


