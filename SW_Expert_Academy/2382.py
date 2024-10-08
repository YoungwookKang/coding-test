import sys
sys.stdin = open("2382_input.txt", "r")

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

T = int(input())


def solve(n, m, group, board):
    answer = 0


    for cnt in range(1,m+1):
        # print(cnt)
        new_board = [[[] for _ in range(n)] for _ in range(n)]
        temp = {}
        for ele in group:
            i, j = ele
            num, d = group[ele]

            # print(f'움직이기 전: {i, j, num, d}')
            # 움직임
            nx, ny = i + dx[d], j + dy[d]

            # 가장자리면 방향전환
            if 0 == nx or 0 == ny or n-1 == nx or n-1 == ny:
                num = num // 2
                # 방향전환
                # d가 2이면 1, 1이면 2, 3이면 4, 4이면 3
                if d == 1:
                    d = 2  # 위쪽 -> 아래쪽
                elif d == 2:
                    d = 1  # 아래쪽 -> 위쪽
                elif d == 3:
                    d = 4  # 왼쪽 -> 오른쪽
                elif d == 4:
                    d = 3  # 오른쪽 -> 왼쪽
            # print(f'움직인 후: {nx, ny, num, d}')
            # 군집 사라졌으면 패스
            if num == 0:
                continue

            # 군집 보드에 작성
            if new_board[nx][ny]:

                if new_board[nx][ny][2] > num:
                    new_board[nx][ny][0] += num
                else:
                    new_board[nx][ny][0] += num
                    new_board[nx][ny][1] = d
                    new_board[nx][ny][2] = num
                # print(f'{nx, ny}에서 합치기 num, d = {new_board[nx][ny][0], new_board[nx][ny][1]}')
            else:
                new_board[nx][ny] = [num, d, num]
                # print(f'{nx, ny}에 새로운 값 넣기 num, d = {num, d}')

        for x in range(n):
            for y in range(n):
                if new_board[x][y]:
                    temp[(x, y)] = [new_board[x][y][0], new_board[x][y][1]]
        board = new_board
        group = temp

        # for ele in board:
        #     print(ele)


    for i in range(n):
        for j in range(n):
            if board[i][j]:
                answer += board[i][j][0]


    return answer


for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(k)]
    groups = {}
    for ele in temp:
        groups[(ele[0], ele[1])] = [ele[2], ele[3]]
    board = [[[] for _ in range(n)] for _ in range(n)]
    for ele in groups:
        i, j = ele
        num, d = groups[ele]
        board[i][j] = [num, d]

    # for ele in board:
    #     print(ele)

    result = solve(n, m, groups, board)

    print(f'#{test_case} {result}')

