
import sys
sys.stdin = open("4013_input.txt", "r")

T = int(input())

def lotate(idxs, idx, dir):
    if dir > 0:
        idxs[idx] = (idxs[idx] - 1) % 8
    else:
        idxs[idx] = (idxs[idx] + 1) % 8
    return idxs


def solve(_m1, _m2, _m3, _m4, _orders):
    total = 0
    idxs = [0,0,0,0, 0]

    for _order in _orders:
        idx, dir = _order
        if idx == 1:
            if _m1[(idxs[1] + 2) % 8] != _m2[(idxs[2] - 2) % 8]:
                if _m2[(idxs[2] + 2) % 8] != _m3[(idxs[3] - 2) % 8]:
                    if _m3[(idxs[3] + 2) % 8] != _m4[(idxs[4] - 2) % 8]:
                        lotate(idxs, 4, -1 * dir)
                    lotate(idxs, 3, dir)
                lotate(idxs, 2, -1 * dir)
            lotate(idxs, 1, dir)
        elif idx == 2:
            if _m1[(idxs[1] + 2) % 8] != _m2[(idxs[2] - 2) % 8]:
                lotate(idxs, 1, -1 * dir)
            if _m2[(idxs[2] + 2) % 8] != _m3[(idxs[3] - 2) % 8]:
                if _m3[(idxs[3] + 2) % 8] != _m4[(idxs[4] - 2) % 8]:
                    lotate(idxs, 4, dir)
                lotate(idxs, 3, -1 * dir)
            lotate(idxs, 2, dir)
        elif idx == 3:
            if _m3[(idxs[3] + 2) % 8] != _m4[(idxs[4] - 2) % 8]:
                lotate(idxs, 4, -1 * dir)
            if _m2[(idxs[2] + 2) % 8] != _m3[(idxs[3] - 2) % 8]:
                if _m1[(idxs[1] + 2) % 8] != _m2[(idxs[2] - 2) % 8]:
                    lotate(idxs, 1, dir)
                lotate(idxs, 2, -1 * dir)
            lotate(idxs, 3, dir)
        else:
            if _m3[(idxs[3] + 2) % 8] != _m4[(idxs[4] - 2) % 8]:
                if _m2[(idxs[2] + 2) % 8] != _m3[(idxs[3] - 2) % 8]:
                    if _m1[(idxs[1] + 2) % 8] != _m2[(idxs[2] - 2) % 8]:
                        lotate(idxs, 1, -1 * dir)
                    lotate(idxs, 2, dir)
                lotate(idxs, 3, -1 * dir)
            lotate(idxs, 4, dir)

        total = _m1[idxs[1]] + (2 * _m2[idxs[2]]) + (4 * _m3[idxs[3]]) + (8 * _m4[idxs[4]])

    return total

for test_case in range(1, T + 1):
   K = int(input())
   m1 = list(map(int, input().split()))
   m2 = list(map(int, input().split()))
   m3 = list(map(int, input().split()))
   m4 = list(map(int, input().split()))

   orders = [list(map(int, input().split())) for _ in range(K)]
   result = solve(m1,m2,m3,m4,orders)
   print(f"#{test_case} {result}")