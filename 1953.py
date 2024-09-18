from collections import deque
import sys

sys.stdin = open("1953_input.txt", "r")

T = int(input())

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solve(n, m, r, c, l, board):
    answer = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    # bfs 써서 그 시간동안 돌아다닌 경로 총 수
    q = deque()
    q.append((r,c,1))
    visited[r][c] = True

    up = [1,2,4,7]
    down = [1,2,5,6]
    left = [1,3,6,7]
    right = [1,3,4,5]

    while q:
        x, y, cnt = q.popleft()
        if cnt <= l:
            answer += 1
        else:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if i == 0 and board[nx][ny] in down and board[x][y] in up:
                    q.append((nx,ny,cnt+1))
                    visited[nx][ny] = True
                elif i == 1 and board[nx][ny] in up and board[x][y] in down:
                    q.append((nx,ny,cnt+1))
                    visited[nx][ny] = True
                elif i == 2 and board[nx][ny] in right and board[x][y] in left:
                    q.append((nx,ny,cnt+1))
                    visited[nx][ny] = True
                elif i == 3 and board[nx][ny] in left and board[x][y] in right:
                    q.append((nx,ny,cnt+1))
                    visited[nx][ny] = True



    return answer

for test_case in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    result = solve(n, m, r, c, l, board)
    print(f'#{test_case} {result}')
