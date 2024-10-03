import copy
import sys
sys.stdin = open("2112_input.txt", "r")

from itertools import combinations, product

T = int(input())

def check(_board, d, w, k):
    # print(f'k = {k}')
    # for e in _board:
        # print(e)
    for j in range(w):
        max_cnt = 0
        cnt = 1
        for i in range(1,d):
            if _board[i][j] == _board[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        # print(f'{j}열의 max_cnt = {max_cnt}')

        if max_cnt < k:
            return False
    return True

def solve(curr, board, d, w, k):
    result = False
    if curr == 0:
        # print(f'curr = {curr}')
        return check(board, d, w, k)
    elif curr == 1:
        # print(f'curr = {curr}')
        for i in range(d):
            original_row = board[i][:]  # 현재 행의 복사본 저장
            for j in range(w):
                board[i][j] = 0
            if check(board, d, w, k):
                board[i] = original_row  # 원래 상태로 복원
                return True
            for j in range(w):
                board[i][j] = 1
            if check(board, d, w, k):
                board[i] = original_row  # 원래 상태로 복원
                return True
            board[i] = original_row  # 원래 상태로 복원
    else:
        for ele in combinations(range(d), curr):
            for selection in product([0,1], repeat=len(ele)):
                # print(f"ele = {ele}, selection = {selection}")
                original_rows = {i: board[i][:] for i in ele}
                for i, row_idx in enumerate(ele):
                    for j in range(w):
                        board[row_idx][j] = selection[i]
                if check(board, d, w, k):
                    # print(f'됨 {ele, selection}')
                    for i in ele:
                        board[i] = original_rows[i]  # 원래 상태로 복원
                    return True
                for i in ele:
                    board[i] = original_rows[i]  # 원래 상태로 복원
    return result

for test_case in range(1, T + 1):
    d, w, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(d)]
    left = 0
    right = k
    while left < right:
        curr = (right + left) // 2
        can_do = solve(curr, board, d, w, k)
        if can_do:
            right = curr
        else:
            left = curr + 1
    # print(check(board, d, w, k))
    answer = left
    print(f"#{test_case} {answer}")




