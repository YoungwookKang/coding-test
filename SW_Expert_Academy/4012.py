from itertools import combinations
import sys
sys.stdin = open("4012_input.txt", "r")

T = int(input())
def backtrack(depth, idx, _board, _n):
    global answer
    # 끝에 도달
    if depth == _n // 2:
        # print(visit)
        a_val = 0
        b_val = 0
        for i in range(_n):
            for j in range(i + 1,_n):
                if visit[i] and visit[j]:
                    a_val += _board[i][j] + _board[j][i]
                elif not visit[i] and not visit[j]:
                    b_val += _board[i][j] + _board[j][i]

        answer = min(answer, abs(a_val - b_val))
    else:
        # range를 index 부터 시작하게 해서 불필요한 중복 제거
        for i in range(idx,_n):
            visit[i] = True
            # 새로운 음식 추가
            backtrack(depth+1, i + 1, _board, _n)
            # 재귀시 visit 복원
            visit[i] = False

def solve(_n, _board):
    global answer
    answer = float('inf')
    backtrack(0, 0, _board, _n)


    return answer

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N


    result = solve(N, board)
    print(f'#{test_case} {result}')