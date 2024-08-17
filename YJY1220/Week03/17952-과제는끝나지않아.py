#17952 - 과제는 끝나지 않아
# memory: ,times: ,lang: python3
# 스택 사용 -> 현재 진행 과제, 완료 과제 나눠서 계산

import sys 

# 시간초과 해결 
N = int(sys.stdin.readline().rstrip()) # N : 전체 시간 

subject = [] #현재 진행 중 과제 
completed = [] #완료 과제 

for _ in range(N):
    score = list(map(int, sys.stdin.readline().rstrip().split())) #과제 정보 

    if score[0] == 1:
        subject.append([score[1], score[2]-1]) #진행 중 과제 남은 시간 1분씩 줄이기 
    elif score[0] == 0:
        if len(subject) != 0:
            subject[-1][1] -= 1
    # 과제 완료 여부 확인 
    if subject and subject[-1][1] == 0:
        score_plus = subject.pop()
        completed.append(score_plus[0]) # 점수만 추가

cnt = 0
for i in completed:
    cnt += i

print (cnt)
