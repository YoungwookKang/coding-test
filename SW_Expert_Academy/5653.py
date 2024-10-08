
import sys

sys.stdin = open("5653_input.txt", "r")

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



# 비활성화 되어 있는 시간 = cell[3] <= t < cell[3] + cell[2]
# 활성화 되어 있는 시간 = cell[3] + cell[2] <= t < cell[3] + cell[2] + cell[2]
def solve (_n, _m, _k, _not_opened_cells):
    alive_cells = 0
    dead_cell = set()
    _opened_cells = {}

    for t in range(1, _k + 1):
        _next_open_cells = {}
        _next_not_opened_cells = {}

        for _opened_cell in _opened_cells:
            if _opened_cells[_opened_cell][0] + _opened_cells[_opened_cell][1] + 1 == t:
                for i in range(4):
                    nx = _opened_cell[0] + dx[i]
                    ny = _opened_cell[1] + dy[i]
                    if (nx, ny) not in dead_cell and (nx, ny) not in _opened_cells and (nx, ny) not in _not_opened_cells:
                        if (nx, ny) in _next_not_opened_cells:
                            _next_not_opened_cells[(nx, ny)] = [max(_opened_cells[_opened_cell][0], _next_not_opened_cells[(nx, ny)][0]), t]
                        else:
                            _next_not_opened_cells[(nx, ny)] = [_opened_cells[_opened_cell][0], t]

            if (_opened_cells[_opened_cell][0] * 2) + _opened_cells[_opened_cell][1] == t:
                dead_cell.add(_opened_cell)
            else:
                _next_open_cells[_opened_cell] = _opened_cells[_opened_cell]

        for _not_opened_cell in _not_opened_cells:
            if _not_opened_cells[_not_opened_cell][0] + _not_opened_cells[_not_opened_cell][1] == t:
                _next_open_cells[_not_opened_cell] = _not_opened_cells[_not_opened_cell]
            else:
                _next_not_opened_cells[_not_opened_cell] = _not_opened_cells[_not_opened_cell]

        _opened_cells = _next_open_cells
        _not_opened_cells = _next_not_opened_cells
        # 계산
        alive_cells = len(_opened_cells) + len(_not_opened_cells)


    return alive_cells

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    not_opened_cells = {}
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                not_opened_cells[(i, j)] = [board[i][j], 0]


    result = solve(N, M, K, not_opened_cells)
    print(f"#{test_case} {result}")