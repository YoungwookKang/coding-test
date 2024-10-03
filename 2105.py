import sys
sys.stdin = open("2105_input.txt", "r")

dx = [1, 1, -1, -1]  # 대각선 방향 x 좌표 이동 (오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위)
dy = [1, -1, -1, 1]  # 대각선 방향 y 좌표 이동


def dfs(x, y, start_x, start_y, direction, count, dessert_set, board, N):
    global max_dessert

    # 이미 시작점으로 돌아왔을 때, 디저트 최대 개수 갱신
    if direction == 3 and x == start_x and y == start_y and count > 2:
        max_dessert = max(max_dessert, count)
        return

    # 4방향 대각선 탐색
    for i in range(direction, direction + 2):  # 현재 방향과 다음 방향만 탐색
        if i >= 4:  # 4 이상의 방향은 없으므로 무시
            continue
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] not in dessert_set:
            dessert_set.add(board[nx][ny])
            dfs(nx, ny, start_x, start_y, i, count + 1, dessert_set, board, N)
            dessert_set.remove(board[nx][ny])


def solve(board, N):
    global max_dessert
    max_dessert = -1

    for i in range(N):
        for j in range(N):
            # 한 카페에서 출발하여 투어 시작
            dfs(i, j, i, j, 0, 0, set([board[i][j]]), board, N)

    return max_dessert


# 입력 처리
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = solve(board, N)
    print(f'#{test_case} {result}')
