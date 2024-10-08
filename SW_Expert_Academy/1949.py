import sys
sys.stdin = open("1949_input.txt", "r")

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(board, x,y, n, k, can_remove, curr_road):
    global max_road
    # print(f"방문 {x,y, curr_road}")
    max_road = max(curr_road, max_road)

    for d in range(4):

        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
            # print(f'nx,ny = {nx},{ny}')
            # 언제 산을 깎으려는지가 중요해.
            # 일단 나보다 낮으면 그냥 넘어가 나보다 높으면 산을 깎고 공사했다는 것을 표시해
            if board[nx][ny] < board[x][y]:
                visit[nx][ny] = True
                dfs(board, nx, ny, n, k, can_remove, curr_road + 1)
                visit[nx][ny] = False
            elif can_remove:
                # print(f"{nx,ny} 깎아야함")
                for i in range(1,k+1):
                    board[nx][ny] -= i
                    if board[nx][ny] < board[x][y]:
                        visit[nx][ny] = True
                        dfs(board, nx, ny, n, k, False, curr_road + 1)
                        visit[nx][ny] = False
                    board[nx][ny] += i


for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    top = []
    top_height = 0
    for i in range(n):
        for j in range(n):
            top_height = max(top_height, board[i][j])

    for i in range(n):
        for j in range(n):
            if board[i][j] == top_height:
                top.append([i, j])
    max_road = 0

    for tx, ty in top:
        # print(f"봉우리 {tx, ty}")
        visit = [[False for _ in range(n)] for _ in range(n)]
        visit[tx][ty] = True
        dfs(board, tx, ty, n, k, True, 1)

    print(f"#{test_case} {max_road}")
