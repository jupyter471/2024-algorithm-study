T = int(input())
movement = [(1,0),(0,-1),(-1,0),(0,1)]   #하좌상우 (시계방향)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = int(input())
    #size x size - 시계방향으로
    snail = [[0] * size for _ in range(size)]
    num = 1
    move_index = 0
    for index in range(size):
        snail[0][index] = str(num)
        num += 1
    #이동
    c_row = 0
    c_col = size-1
    i = size-1
    while i >= 1:
        for _ in range(2):
            for _ in range(i):
                c_row += movement[move_index % 4][0]
                c_col += movement[move_index % 4][1]
                snail[c_row][c_col] = str(num)
                num += 1
            move_index += 1
        i -= 1
    print(f'#{test_case}')
    for i in range(size):
        print(' '.join(snail[i]))
