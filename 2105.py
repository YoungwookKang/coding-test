import sys

sys.stdin = open("2105_input.txt", "r")

T = int(input())

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

visit = [0 for _ in range(101)]



def move(board, x, y, start_x, start_y, d, cnt):
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and visit[board[nx][ny]] == 0:
        # print(f"{nx,ny}로 움직임 {d}방향")
        visit[board[nx][ny]] = 1
        dfs(board, nx, ny, start_x, start_y, d, cnt + 1, True)
        visit[board[nx][ny]] = 0


def dfs(board, x, y, start_x, start_y, direction, curr_cnt, is_moved):
    global answer
    # print(x, y, direction)
    # print(visit)
    if direction == 3 and x == start_x and y == start_y:
        answer = max(curr_cnt, answer)
        # print(answer)
        return
    if direction == 2 and answer > curr_cnt * 2:  # 더 작은 직사각형 제거
        return
    # 세 변 그리기 시작한 후부터는 바향 안꺾음
    if direction == 2 and start_x + start_y == y + x:  # 세 변 그렸으면
        dfs(board, x, y, start_x, start_y, direction + 1, curr_cnt, False) # 방향 꺾어서 직사각형 완성시키기
        return
    move(board, x, y, start_x, start_y, direction, curr_cnt)
    if is_moved and direction < 2:
        # print(f'{direction + 1}방향으로 방향 꺾음')
        dfs(board, x, y, start_x, start_y, direction + 1, curr_cnt, False)


def solve(board, n):
    for i in range(n - 2):
        for j in range(1, n - 1):
            # print(f"새로운 거 시작 {i, j}")
            dfs(board, i, j, i,j,0, 0, False)


for test_case in range(1, T + 1):
    answer = -1
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    solve(board, n)

    print(f'#{test_case} {answer}')
