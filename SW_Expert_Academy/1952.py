import sys
sys.stdin = open("1952_input.txt", "r")

T = int(input())
def solve(prices, plans):
    annual_prices = prices[3]
    new_plans = []
    for i in range(len(plans)):
        new_plans.append(min(prices[1], plans[i] * prices[0]))
    dp = []
    for i in range(len(new_plans)):
        if i == 0:
            dp.append(min(prices[2], new_plans[i]))
        elif i < 3:
            dp.append(min(prices[2], new_plans[i] + dp[i - 1]))
        else:
            dp.append(min(prices[2] + dp[i - 3], dp[i - 1] + new_plans[i]))
        # print(i)
        # print(dp)
    answer = min(annual_prices, dp[len(dp) - 1])
    return answer

for test_case in range(1, T + 1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))

    result = solve(prices, plans)
    print(f"#{test_case} {result}")