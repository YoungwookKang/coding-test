import sys
sys.stdin = open("5648_input.txt", "r")

# 상하좌우
dx = [-0.5, 0.5, 0, 0]
dy = [0, 0, -0.5, 0.5]
def solve(elements, n):
   return 0

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    # x축 y축 체크
    elements = [list(map(int, input().split())) for _ in range(n)]
    # 0.5초씩 움직이면 됨

    result = solve(elements, n)
    print(f'#{test_case} {result}')