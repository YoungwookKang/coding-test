import sys
from collections import deque
sys.stdin = open("5650_input.txt", "r")

# 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
T = int(input())


def is_boundary(x,y,d, n):
    if 0 <= x < n and 0 <= y < n:
        return x,y, (d+2) % 4, n
    else:
        return x,y,d,n

def move(start_i,start_j,d,board,n, black_hole, worm_hole):
    hit = 0
    q = deque()
    q.append((start_i,start_j,d))
    while q:
        x,y,d = q.popleft()
        # print(f'{x,y,d}')
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            nd = (d + 2) % 4
            # print(f'경계 부딪힘 x,y,nx,ny,d,nd {x, y, nx, ny, d, nd}')
            hit +=1
            q.append((nx, ny, nd))
            continue
        # print(f"nx,ny board[nx][ny]= {nx, ny, board[nx][ny]} ")
        if board[nx][ny] == -1 or (nx == start_i and ny == start_j):
            # print(f'도착 nx,ny = {nx},{ny}')
            continue
            # 경계에 부딪히거나

        # 벽에 부딪히거나 (방향까지만 바꿈
        elif board[nx][ny] == 1:
            # print(f'벽1')
            if d == 0 or d == 3:
                nd = (d+2) % 4
            elif d == 1:
               nd = 0
            else:
                nd = 3
            hit += 1
            q.append((nx, ny, nd))
            continue
        elif board[nx][ny] == 2:
            # print('벽2')
            if d == 2 or d == 3:
                nd = (d+2) % 4
            elif d == 1:
               nd = 2
            else:
                nd = 3
            hit += 1
            q.append((nx, ny, nd))
            continue
        elif board[nx][ny] == 3:
            # print("벽 3")
            if d == 2 or d == 1:
                nd = (d+2) % 4
            elif d == 0:
               nd = 1
            else:
                nd = 2
            hit += 1
            q.append((nx, ny, nd))
            continue
        elif board[nx][ny] == 4:
            # print("벽 4")
            if d == 0 or d == 1:
                nd = (d+2) % 4
            elif d == 2:
               nd = 1
            else:
                nd = 0
            hit += 1
            q.append((nx, ny, nd))
            continue
        elif board[nx][ny] == 5:
            # print("벽 5")
            nd = (d + 2) % 4
            hit += 1
            q.append((nx, ny, nd))
            continue

        # 웜홀 만나거나
        elif board[nx][ny] >= 6:
            # print("원홀")
            after_worm_hole_x , after_worm_hole_y = worm_hole[(nx,ny)]
            q.append((after_worm_hole_x, after_worm_hole_y, d))
            continue

        elif board[nx][ny] == 0:
            q.append((nx, ny, d))


    return hit
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_count = 0
    black_hole = []
    worm_hole = {}
    temp = {}
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                black_hole.append((i, j))
            if board[i][j] >= 6:
                if board[i][j] in temp:
                    temp[board[i][j]].append((i, j))
                else:
                    temp[board[i][j]] = [(i, j)]
    for ele in temp:
        h1x,h1y = temp[ele][0]
        h2x,h2y = temp[ele][1]
        worm_hole[(h1x,h1y)] = (h2x,h2y)
        worm_hole[(h2x,h2y)] = (h1x,h1y)
    # for ele in board:
    #     print(ele)
    #
    # print(worm_hole)
    # # print(black_hole)
    # print(temp)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                for d in range(4):
                    # print(f'{i,j}에서 {d}로 출발')
                    cnt = move(i,j,d,board,n, black_hole, worm_hole)
                    max_count = max(max_count, cnt)
    # cnt = move(2, 3, 3, board, n, black_hole, worm_hole)

    print(f"#{test_case} {max_count}")