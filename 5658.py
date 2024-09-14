# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys

sys.stdin = open("5658_input.txt", "r")

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