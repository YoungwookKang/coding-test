from collections import deque

import sys
sys.stdin = open("2117_input.txt", "r")

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def calculate(i,j,k,m,board):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()

    q.append((i,j, 1))
    visited[i][j] = True
    cost = k * k + (k-1) * (k-1)
    profit = 0

    count = 0
    while q:

        x,y, depth = q.popleft()
        # print(f"{x, y} 검사")

        if board[x][y] == 1:
            profit += m
            count += 1
            # print(f"{x,y}에 집있음 {count}")


        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and depth < k:
                q.append((nx,ny, depth + 1))
                visited[nx][ny] = True


    if profit >= cost:
        # print(f"cost = {cost}, profit = {profit} count = {count}")
        return count
    else:
        return 0





def solve(n,m,board):
    answer = 0
    k = 0
    # 완전히 꽉 채울 수 있는 최소 크기
    # 여기까지 증가시키면서 검사하면 됨
    if n % 2 == 0:
        max_k = n + 1
    else:
        max_k = n
    # print(f"max k = {max_k}")
    for k in range(max_k, 0, -1):
        if answer == (k * k) + (k - 1) * (k - 1):
            continue
        for i in range(n):
            if answer == (k * k) + (k - 1) * (k - 1):
                continue
            for j in range(n):
                if answer == (k * k) + (k-1) * (k-1):
                    continue
                # print(f"k,i,j = {k,i,j}")
                temp = calculate(i,j,k,m,board)
                answer = max(temp,answer)


    return answer

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    result = solve(n, m, board)

    print(f"#{test_case} {result}")