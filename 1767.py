import sys

sys.stdin = open("1767_input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def can_do(board, x, y, d, n):
    wires = []
    nx, ny = x + dx[d], y + dy[d]
    while True:
        if 0 > nx or n <= nx or 0 > ny or n <= ny:
            break
        if board[nx][ny] != 0:
            return False, []
        wires.append((nx, ny))
        nx, ny = nx + dx[d], ny + dy[d]

    return True, wires


def dfs(core_list, core_idx, n, board, connected_core, current_length):
    global max_core, max_core_min_length
    # print(connected_core, current_length)
    # if connected_core == 5:
    #     for ele in board:
    #         print(ele)
    # 다 탐색
    if core_idx == len(core_list):
    # 모든 코어를 탐색한 후 최대 코어랑 쵀대 코어 최소 전선 구하기
        if connected_core > max_core:
            max_core = connected_core
            max_core_min_length = current_length
        elif connected_core == max_core:
            max_core_min_length = min(max_core_min_length, current_length)
        return
    x, y = core_list[core_idx]
    for d in range(4):
        # 전선 설치 가능?
        condition, wires = can_do(board, x, y, d, n)
        # print(f'core_index = {core_idx}, x = {x}, y = {y}')
        # print(condition)
        # print(wires)
        # 가능하면설치
        if condition:
            for wx, wy in wires:
                # 전선은 2로 표시
                board[wx][wy] = 2
            # 다음 코어 탐색
            dfs(core_list, core_idx + 1, n, board, connected_core + 1, current_length + len(wires))
            # 전선 복구
            for wx, wy in wires:
                board[wx][wy] = 0
    dfs(core_list, core_idx + 1, n, board, connected_core, current_length)


def solve(n, board):
    global max_core, max_core_min_length
    core_list = []
    # 가장자리에 있는 코어는 이미 전원이 연결된 것으로 간주
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i][j] == 1:
                core_list.append((i, j))
    max_core = 0
    max_core_min_length = float('inf')
    dfs(core_list, 0, n, board, 0, 0)
    return max_core_min_length


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = solve(n, board)
    print(f'#{test_case} {result}')
