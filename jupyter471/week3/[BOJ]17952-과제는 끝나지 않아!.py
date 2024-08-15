"""
과제가 생기자마자 시작
새로운 과제가 생기는 경우 기존 과제 중단 후 새로운 과제
과제가 끝나면 이전에 하던 과제 재개 stack
-> 점수 구하기

3
1 100 3 : 과제 유무, 만점, 소요되는 시간
0
0
"""
import sys
n = int(input())
work = []
for _ in range(n):
    work.append(list(map(int, sys.stdin.readline().split())))

start = []
score = 0
#[소요시간, 점수]
for w in work:
    if w[0] == 1:
        if w[2] == 1:
            score += w[1]
            continue
        start.append([w[2]-1, w[1]])

    else:
        #[0]
        if start:  #첨에 이거 안해서 런타임에러남
            now = start.pop()
            if now[0] == 1:
                score += now[1]
            else:
                start.append([now[0]-1,now[1]])
print(score)
