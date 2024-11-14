def test():
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly = 0
            for di in range(M):
                fly += sum(matrix[i + di][j:j + M])
            if fly > maximum:
                maximum = fly

    return maximum


T = int(input())
for t in range(1, T + 1):
    result = test()
    print(f"#{t} {result}")
