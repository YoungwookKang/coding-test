import sys

sys.stdin = open("4008_input.txt", "r")

T = int(input())

def backtrack(total, operators, nums, depth, N):
    global min_answer, max_answer
    if depth == N:
        min_answer = min(min_answer, total)
        max_answer = max(max_answer, total)
    # 근데 이렇게 backtracking 하면 연산자 수를 리스트로 관리해서 재귀 호출 후 연산자 개수를 복원해야함

    # 더하기
    if operators[0] > 0:
        operators[0] -= 1
        backtrack(total + nums[depth], operators, nums, depth + 1, N)
        operators[0] += 1
    # 빼기
    if operators[1] > 0:
        operators[1] -= 1
        backtrack(total - nums[depth], operators, nums, depth + 1, N)
        operators[1] += 1
    # 곱하기
    if operators[2] > 0:
        operators[2] -= 1
        backtrack(total * nums[depth], operators, nums, depth + 1, N)
        operators[2] += 1
    # 나누기
    if operators[3] > 0:
        operators[3] -= 1
        if total >= 0:
            backtrack(total // nums[depth], operators, nums, depth + 1, N)
        else:
            backtrack(-(-total // nums[depth]), operators, nums, depth + 1, N)
        operators[3] += 1

def backtracking(depth, total, plus, minus, mul, div, nums, N):
    global min_answer, max_answer

    if depth == N:
        min_answer = min(min_answer, total)
        max_answer = max(max_answer, total)
        return

    if plus > 0:
        backtracking(depth + 1, total + nums[depth], plus - 1, minus, mul, div, nums, N)
    if minus > 0:
        backtracking(depth + 1, total - nums[depth], plus, minus - 1, mul, div, nums, N)
    if mul > 0:
        backtracking(depth + 1, total * nums[depth], plus, minus, mul - 1, div, nums, N)
    if div > 0:
        if total >= 0:
            backtracking(depth + 1, total // nums[depth], plus, minus, mul, div - 1, nums, N)
        else:
            backtracking(depth + 1, -(-total // nums[depth]), plus, minus, mul, div - 1, nums, N)


def solve(N, operators, nums):
    global min_answer, max_answer

    min_answer = 100000000
    max_answer = -100000000

    backtrack(nums[0],operators, nums, 1, N)

    # 이렇게 하면 재귀호출 시 복원을 안해도 됨
    plus, minus, mul, div = operators
    backtracking(1, nums[0], plus, minus, mul, div, nums, N)

    return max_answer - min_answer

for test_case in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))

    nums = list(map(int, input().split()))
    result = solve(N, operators, nums)
    print(f"#{test_case} {result}")
