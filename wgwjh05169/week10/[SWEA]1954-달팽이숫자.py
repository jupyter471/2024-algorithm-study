def test():
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    loop = N // 2 if N % 2 == 0 else N // 2 + 1

    cnt = 1
    for k in range(loop):
        lowest = 0 + k
        highest = N - k - 1

        for idx in range(0 + k, N - k):
            snail[lowest][idx] = cnt
            cnt += 1
        cnt -= 1

        for idx in range(0 + k, N - k):
            snail[idx][highest] = cnt
            cnt += 1
        cnt -= 1

        for idx in range(N - k - 1, 0 + k - 1, -1):
            snail[highest][idx] = cnt
            cnt += 1
        cnt -= 1

        for idx in range(N - k - 1, 0 + k, -1):
            snail[idx][lowest] = cnt
            cnt += 1

    for i in range(N):
        print(*snail[i], sep=' ')


T = int(input())
for t in range(1, T + 1):
    print(f'#{t}')
    test()
