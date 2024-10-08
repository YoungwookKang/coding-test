from itertools import product


def calculate_time(people, stairs, selections):
    # selection = (0, 0, 0, 1, 1, 1)
    # people = [(0, 1), (0, 2), (1, 2), (2, 1), (2, 3), (4, 0)]
    # stairs = [(1, 4, 3), (4, 2, 5)]
    times = [[] for _ in range(2)]  # 두 계단에 대한 도착 시간 리스트
    for i, stair_idx in enumerate(selections):
        px, py = people[i]
        sx, sy, sd = stairs[stair_idx]
        distance = abs(px - sx) + abs(py - sy)
        times[stair_idx].append(distance)

    # times = [[4, 3, 2],[3, 3, 2]]

    max_time = 0
    for stair_idx in range(2):
        sx, sy, sd = stairs[stair_idx]
        # 먼저 도착한 순서
        times[stair_idx].sort()

        finish_times = []
        for i, arrival_time in enumerate(times[stair_idx]):
            # 계단에 오는 사람이 3명 이하면 그냥 도착시간 + 1 (이떄부터 내려감) + 계단길이
            if i < 3:
                finish_times.append(arrival_time + 1 + sd)
            # 계단을 이용하는 사람이 4명 이상이면
            else:
                if arrival_time >= finish_times[i - 3]:
                    finish_times.append(arrival_time + 1 + sd)
                else:
                    finish_times.append(finish_times[i - 3] + sd)

        if finish_times:
            max_time = max(max_time, finish_times[-1])

    return max_time


def solve(test_cases):
    results = []
    test_case = 0
    for (N, grid) in test_cases:
        test_case += 1
        people = []
        stairs = []

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    people.append((r, c))
                elif grid[r][c] > 1:
                    stairs.append((r, c, grid[r][c]))
        min_time = float('inf')

        for selections in product([0, 1], repeat=len(people)):
            time = calculate_time(people, stairs, selections)
            min_time = min(min_time, time)

        results.append(f"#{test_case} {min_time}")

    return results

#import sys
#sys.stdin = open("sample_input.txt", "r")
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    test_cases.append((N, grid))

results = solve(test_cases)

for result in results:
    print(result)
