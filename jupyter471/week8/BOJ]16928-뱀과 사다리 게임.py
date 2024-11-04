"""
1부터 100
10x10
사다리 -> 위로
뱀 -> 아래로
100번칸 넘어가면 이동 X -> 딱 맞춰야됨
이동범위 1<= <=6
1~6까지 갔을 때 멀리갈 수 있는 거 -> 없다면
"""
from collections import defaultdict,deque
snake = defaultdict(int)
ladder = defaultdict(int)
m,n  = map(int,input().split())

for _ in range(m):
    p,q = map(int,input().split())
    ladder[p] = q


for _ in range(n):
    p,q = map(int,input().split())
    snake[p] = q


dice_count = [[float('inf')] * 10 for _ in range(10)]  #횟수 저장

#1~6까지
def bfs():
    dq = deque()
    dq.append(1)
    dice_count[0][0] = 0
    while dq:
        curr = dq.popleft()
        curr_r, curr_c = find_location(curr)
        for i in range(1,7):
            nxt = curr + i
            if nxt <= 100:
                nxt_r, nxt_c = find_location(nxt)
                count = dice_count[curr_r][curr_c] + 1
                if dice_count[nxt_r][nxt_c] > count:  #이동조건
                    dice_count[nxt_r][nxt_c] = count
                    if nxt in ladder: #사다리타고 이동
                        final = ladder[nxt]
                        final_r, final_c = find_location(final)

                        if dice_count[final_r][final_c] > dice_count[nxt_r][nxt_c]:
                            dice_count[final_r][final_c] = dice_count[nxt_r][nxt_c]
                            dq.append(final)
                    elif nxt in snake:
                        final = snake[nxt]
                        final_r, final_c = find_location(final)
                        if dice_count[final_r][final_c] >  dice_count[nxt_r][nxt_c]:
                            dice_count[final_r][final_c] = dice_count[nxt_r][nxt_c]
                            dq.append(final)
                    else:
                        dq.append(nxt)


def find_location(n):
    r,c = 0,0
    if n % 10 == 0:
        r = n // 10 - 1
        c = 9
    else:
        r = n // 10
        c = n % 10 -1
    return r,c

bfs()
print(dice_count[9][9])