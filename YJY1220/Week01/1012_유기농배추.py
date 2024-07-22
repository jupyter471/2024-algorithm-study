#BOJ - 1012.유기농배추
#memory : 31120KB, times: 304ms, lang : python
#처음에 재귀로 dfs함수 내 재호출 -> RuntimeError(RecursionError)
#이후 스택으로 마지막 위치 = 현재위치 지정하는 식으로 변경 

def dfs(x, y, base, check, n, m):
    array = [(x, y)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while array: # 빌 때까지 계속 돎
        cur_x, cur_y = array.pop() # 현재위치 설정 - 이전의 마지막 위치임
        if check[cur_x][cur_y] == 1: # 이미 방문 시 패스 
            continue
        check[cur_x][cur_y] = 1 # 안한 곳이니까 1 

        for i in range(4):
            next_x = cur_x + dx[i] # 인접 위치 계산 + 3까지
            next_y = cur_y + dy[i]
            # 배추밭 범위 있는지 확인 & 배추 있는지 확인 & 방문했는지 확인 
            if 0 <= next_x < n and 0 <= next_y < m and base[next_x][next_y] == 1 and check[next_x][next_y] == 0: 
                array.append((next_x, next_y)) # 새로운 좌표 추가

    return 1

# 입력
N = int(input())
res = []
for _ in range(N):
    m, n, k = map(int, input().split())
    base = [[0]*m for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        base[y][x] = 1

    cnt = 0

    # dfs 탐색
    for i in range(n):
        for j in range(m):
            if base[i][j] == 1 and check[i][j] == 0:
                cnt += dfs(i, j, base, check, n, m)

    res.append(cnt)

for result in res:
    print(result)
