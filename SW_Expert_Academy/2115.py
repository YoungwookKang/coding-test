import sys
sys.stdin = open("2115_input.txt", "r")


def calculate_max_profit(worker, c):
    max_profit = 0
    n = len(worker)

    # 모든 조합을 탐색하여 최대 수익 계산
    def dfs(idx, curr_sum, curr_profit):
        nonlocal max_profit
        if curr_sum > c:  # 용량 초과 시, 탐색 중단
            return
        if idx == n:
            max_profit = max(max_profit, curr_profit)
            return
        # 현재 꿀을 선택하거나 선택하지 않는 두 가지 경우로 나누어 탐색
        dfs(idx + 1, curr_sum + worker[idx], curr_profit + worker[idx] ** 2)
        dfs(idx + 1, curr_sum, curr_profit)

    dfs(0, 0, 0)
    return max_profit


def solve(n, m, c, board):
    max_total_profit = 0

    for i in range(n):
        for j in range(n - m + 1):
            # 첫 번째 일꾼이 선택한 벌통
            worker_1 = board[i][j:j + m]
            max_1 = calculate_max_profit(worker_1, c)

            # 두 번째 일꾼이 선택할 벌통의 위치 탐색 (중복되지 않도록)
            for x in range(i, n):
                if x == i:
                    start_col = j + m  # 같은 행에서 겹치지 않도록 시작 지점 설정
                else:
                    start_col = 0
                for y in range(start_col, n - m + 1):
                    worker_2 = board[x][y:y + m]
                    max_2 = calculate_max_profit(worker_2, c)

                    # 두 일꾼의 최대 수익 합산
                    max_total_profit = max(max_total_profit, max_1 + max_2)

    return max_total_profit


# 입력 처리 및 테스트 케이스 실행
T = int(input())
for test_case in range(1, T + 1):
    n, m, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    result = solve(n, m, c, board)
    print(f'#{test_case} {result}')
