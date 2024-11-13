T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    benefit = list(map(int, input().split()))
    max_benefit = 0
    total = 0
    for i in range(n - 1, -1, -1):
        if benefit[i] > max_benefit:
            max_benefit = benefit[i]
        else:
            total += max_benefit - benefit[i]

    print(f'#{test_case} {total}')