T = int(input())
def calculate_password(password):
    sum_num = []
    for i in range(len(password)):
        temp = 0
        for j in range(len(password[0])):
            temp += 16 ** j * password[i][len(password[i]) - 1 - j]
        sum_num.append(temp)

    return sum_num

def solve(_num_list, _n, _k):
    answer_set = set()

    cnt = 0
    for k in range(_n):
        password = [[] for _ in range(4)]
        for i in range(_n):
            for j in range(len(password)):
                password[j].append(_num_list[(i + cnt + (j * _n)) % (4 * _n)])

        temp = calculate_password(password)
        for ele in temp:
            answer_set.add(ele)

        cnt += 1

    answer_list = []
    for ele in answer_set:
        answer_list.append(ele)

    answer_list.sort(reverse=True)

    return answer_list[_k - 1]

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = input()
    temp = [nums[i] for i in range(len(nums))]
    switch_dict = {'0': 0,
                  '1': 1,
                  '2': 2,
                  '3': 3,
                  '4': 4,
                  '5': 5,
                  '6': 6,
                  '7': 7,
                  '8': 8,
                  '9': 9,
                  'A': 10,
                  'B': 11,
                  'C': 12,
                  'D': 13,
                  'E': 14,
                  'F': 15}

    num_list = []
    for i in range(len(temp)):
        num_list.append(switch_dict[temp[i]])

    N = N//4
    result = solve(num_list, N, K)

    print(f'#{test_case} {result}')