"""
주사위 > 지도 : 이동방향 90도 시계
주사위 < 지도 : 이동방향 반시계
주사위 = 지도 : 변화 X
점수 = 지도 값 x 연속해서 이동할 수 있는 칸의 수
각 이동에서 획득하는 점수의 합
이동하고 -> 거기서부터 얼마나 연속?
방향을 바꾸지않고 얼마나 이동할 수 있는지 -> 이게 아니라 숫자가 같은 칸의 수임
"""
import sys
from collections import deque
n,m,k = map(int, sys.stdin.readline().split())

area = []
for _ in range(n):
    area.append(list(map(int, sys.stdin.readline().split())))

direction = {'E' : (0,1), 'W' : (0,-1), 'N' : (-1,0), 'S':(1,0)}
inversed_dir = {'E' : 'W', 'W' : 'E', 'S':'N','N':'S'}  #방향전환용
#동서남북
clock = ['E','S','W','N']  #동남서북
anti_clock = ['W','S','E','N']   #서남동북
dice = [2,1,5,6,4,3]

def turn_dice(dir,dice):
    # dice = [세로 4개(위->아래), 양 날개(왼->오)]
    if dir == 'E':
        new_dice = [dice[0], dice[4], dice[2], dice[5], dice[3], dice[1]]
    elif dir == 'W':
        new_dice = [dice[0], dice[5], dice[2], dice[4], dice[1], dice[3]]
    elif dir == 'S':
        new_dice = [dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]]
    else:
        new_dice = [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]
    return new_dice

#주사위의 이동 점수랑 상관 X
def move(dir,dice,curr):
    #움직이고
    #다이스 변화
    next_r = curr[0] + direction[dir][0]
    next_c = curr[1] + direction[dir][1]
    if not 0 <= next_r < n or not 0 <= next_c < m:
         #방향전환
        dir = inversed_dir[dir]
        #동 <-> 서, 남 <-> 북
        next_r = curr[0] + direction[dir][0]
        next_c = curr[1] + direction[dir][1]
    dice = turn_dice(dir,dice)

    return dir,dice,[next_r,next_c]

def turn_direction(dice,dir,curr):
    num = dice[3]  # 밑면
    if num > area[curr[0]][curr[1]]:
        # 시계방향
        index = clock.index(dir)
        dir = clock[(index + 1) % 4]
    elif num < area[curr[0]][curr[1]]:
        # 반시계방향
        index = anti_clock.index(dir)
        dir = anti_clock[(index + 1) % 4]
    return dir
def count_score(curr):
    visited = [[False] * m for _ in range(n)]
    #comparator와 같은 수를 가진 칸의 개수 세기
    dq = deque()
    dq.append(curr)
    visited[curr[0]][curr[1]] = True
    comparator = area[curr[0]][curr[1]]
    score = 1
    while dq:
        curr = dq.popleft()
        for move in direction.values():
            #동서남북이동
            nxt_r = curr[0] + move[0]
            nxt_c = curr[1] + move[1]
            if 0 <= nxt_r < n and 0 <= nxt_c < m:
                if area[nxt_r][nxt_c] == comparator and not visited[nxt_r][nxt_c] :
                    score += 1
                    visited[nxt_r][nxt_c] = True
                    dq.append([nxt_r,nxt_c])
    return score * comparator

#시작
dir = 'E'
curr = [0,0]
total_score = 0
for i in range(k):
    dir,dice,curr = move(dir,dice,curr)
    total_score += count_score(curr)
    dir = turn_direction(dice,dir,curr)
print(total_score)