def test():
    N = int(input())
    prices = list(map(int, input().split()))
    bounds = [0] * N

    maximum = prices[-1]
    for i in range(N - 1, -1, -1):
        if prices[i] > maximum:
            maximum = prices[i]
        bounds[i] = maximum

    profit = 0
    for i in range(N):
        profit += bounds[i] - prices[i]

    return profit


T = int(input())
for t in range(1, T + 1):
    result = test()
    print(f'#{t} {result}')
