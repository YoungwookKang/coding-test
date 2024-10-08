
# import sys
# sys.stdin = open("4014_input.txt", "r")

T = int(input())

def solve(_board, _x, _n):
    count = 0
    # 각 row나 column 마다 양쪽으로 검사 각자 내리막만 체크 마지막 겹치는지 체크
    for i in range(_n):
        left = [0 for _ in range(_n)]
        right = [0 for _ in range(_n)]
        left_ok = True
        right_ok = True
        for j in range(_n - 1):
            if _board[i][j] <= _board[i][j + 1]:
                continue
            if _board[i][j] > _board[i][j + 1] + 1:
                left_ok = False
                break

            # 1칸 차이나는 내리막
            if j + 1 + _x > _n:
                left_ok = False
                break
            for k in range(_x - 1):
                if _board[i][j+1+k] != _board[i][j+1 + k+1]:
                    left_ok = False
                    break
            if left_ok:
                for k in range(_x):
                    left[j + 1 + k] = 1
        # 오르막
        for j in range(_n - 1, 0, -1):

            if _board[i][j] <= _board[i][j - 1]:
                continue

            if _board[i][j] > _board[i][j - 1] + 1:
                right_ok = False
                break

            # 1칸 차이나는 내리막
            if j - 1 - _x < -1:
                right_ok = False
                break
            for k in range(_x - 1):
                if _board[i][j-1-k] != _board[i][j-1 - (k+1)]:
                    right_ok = False
                    break
            if right_ok:
                for k in range(_x):
                    right[j - 1 - k] = 1

        count_ok = True
        for j in range(_n):
            if left[j] == 1 and right[j] == 1:
                count_ok = False
                break
        if left_ok and right_ok and count_ok:
            count += 1

    for i in range(_n):
        left = [0 for _ in range(_n)]
        right = [0 for _ in range(_n)]
        left_ok = True
        right_ok = True
        for j in range(_n - 1):
            if _board[j][i] <= _board[j + 1][i]:
                continue
            if _board[j][i] > _board[j + 1][i] + 1:
                left_ok = False
                break

            # 1칸 차이나는 내리막
            if j + 1 + _x > _n:
                left_ok = False
                break
            for k in range(_x - 1):
                if _board[j+1+k][i] != _board[j+1 + k+1][i]:
                    left_ok = False
                    break
            if left_ok:
                for k in range(_x):
                    left[j + 1 + k] = 1
        # 오르막
        for j in range(_n - 1, 0, -1):

            if _board[j][i] <= _board[j - 1][i]:
                continue

            if _board[j][i] > _board[j - 1][i] + 1:
                right_ok = False
                break

            # 1칸 차이나는 내리막
            if j - 1 - _x < -1:
                right_ok = False
                break
            for k in range(_x - 1):
                if _board[j-1-k][i] != _board[j-1 - (k+1)][i]:
                    right_ok = False
                    break
            if right_ok:
                for k in range(_x):
                    right[j - 1 - k] = 1

        count_ok = True
        for j in range(_n):
            if left[j] == 1 and right[j] == 1:
                count_ok = False
                break
        if left_ok and right_ok and count_ok:
            count += 1

    return count

for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    result = solve(grid, X, N)

    # print(f' x = {X}')
    # for ele in grid:
    #     print(ele)
    # print()

    print(f'#{test_case} {result}')