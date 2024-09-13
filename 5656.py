import copy
from collections import deque
from itertools import product
import sys

sys.stdin = open("5656_input.txt", "r")

T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def elevate(_board, r, c):
    blocks = [[] for _ in range(c)]
    for j in range(c):
        for i in range(r-1, -1, -1):
            if _board[i][j] > 0:
                blocks[j].append(_board[i][j])

    temp = [[0 for _ in range(c)] for _ in range(r)]
    for j in range(c):
        cnt = 0
        for i in range(r-1, r-1 - len(blocks[j]), -1):
            temp[i][j] = blocks[j][cnt]
            cnt += 1

    return temp



def break_blocks(_board, target, _h, _w):
    q = deque([target])
    temp = copy.deepcopy(_board)

    while q:
        x, y = q.popleft()
        temp[x][y] = 0
        val = _board[x][y]
        for i in range(1,val):
            for j in range(4):
                nx, ny = x + (dx[j] * i), y + (dy[j] * i)
                if 0 <= nx < _h and 0 <= ny < _w and temp[nx][ny] > 0:
                    q.append((nx,ny))
    return temp


def calculate_blocks(_board, selections):
    total = 0
    # print(selections)
    _h, _w = len(_board), len(_board[0])
    for shot in selections:
        get_shot = False
        target = [0, shot]
        for i in range(_h):
            if _board[i][shot] > 0:
                get_shot = True
                target = [i, shot]
                break
        if not get_shot:
            continue

        _board = break_blocks(_board, target, _h, _w)
        _board = elevate(_board, _h, _w)

    for i in range(len(_board)):
        for j in range(len(_board[0])):
            if _board[i][j] > 0:
                total += 1

    # for ele in _board:
    #     print(ele)

    return total

def solve(_N, board):
    max_blocks = len(board) * len(board[0])
    width = []
    for i in range(len(board[0])):
        width.append(i)

    for selections in product(width, repeat=_N):
        blocks = calculate_blocks(board, selections)
        # print()
        if blocks == 0:
            return 0
        max_blocks = min(max_blocks, blocks)


    return max_blocks

for test_case in range(1, T + 1):
   N, W, H = map(int, input().split())
   grid = [list(map(int, input().split())) for _ in range(H)]
   result = solve(N, grid)

   print(f'#{test_case} {result}')