# 1766 - 문제집
# memory: 38308KB, times: 3356ms, lang: python3
# 위상정렬 
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

textbook = []
for _ in range(N+1):
    textbook.append([])
problem = []
for _ in range(N+1):
    problem.append(0)
res = []

# 그래프와 진입차수 정보 저장하기
for i in range(M):
    A, B = map(int, input().split())
    textbook[A].append(B)
    problem[B] += 1

def topological(textbook, problem):
    # 진입차수가 0인 노드를 큐에 넣기
    queue = []
    for i in range(1, N+1):
        if problem[i] == 0:
            queue.append(i)
    
    while queue: # 큐가 빌 때까지 반복
        queue.sort()
        current_node = queue.pop(0) #가장 앞에꺼 꺼내기
        res.append(current_node)
        
        for i in textbook[current_node]: #진입차수 감소 
            problem[i] -= 1
            # 진입차수가 0이 된 노드를 큐에 추가
            if problem[i] == 0:
                queue.append(i)

topological(textbook, problem)
print(*res) #[] 없애기
