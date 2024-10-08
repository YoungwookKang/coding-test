import sys

sys.stdin = open("5644_input.txt", "r")

T = int(input())

dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]
def move(u1, u2, people, t):
    d1 = people[0][t]
    d2 = people[1][t]
    x1, y1 = dx[d1], dy[d1]
    x2, y2 = dx[d2], dy[d2]
    u1 = ((u1[0] + x1), (u1[1] + y1))
    u2 = ((u2[0] + x2), (u2[1] + y2))
    return u1, u2
def calculate_distance(user, bc):
    x, y = user
    d = abs(x - bc[0]) + abs(y-bc[1])
    # print(d)
    if d <= bc[2]:
        return True
    return False

def get_possible_bcs(user, bcs):
    can_use = []
    for i in range(len(bcs)):
        # print(f'use = {user}, bc = {bcs[i]}')
        if calculate_distance(user, bcs[i]):
            # print('가능')
            can_use.append(i)
    return can_use

def calculate_max(arr1, arr2, bcs):
    maxValue = 0
    if len(arr1) > 0 and len(arr2) > 0:
        for ele1 in arr1:
            for ele2 in arr2:
                if ele1 == ele2:
                    maxValue = max(bcs[ele1][3], maxValue)
                else:
                    maxValue = max(bcs[ele1][3] + bcs[ele2][3], maxValue)
    elif len(arr1) > 0:
        for ele1 in arr1:
            maxValue = max(maxValue, bcs[ele1][3])
    elif len(arr2) > 0:
        for ele2 in arr2:
            maxValue = max(maxValue, bcs[ele2][3])

    return maxValue


def solve(people, bcs, M, A, user1, user2):
    max_charge = 0
    # 계산
    arr1 = get_possible_bcs(user1, bcs)
    arr2 = get_possible_bcs(user2, bcs)
    max_charge += calculate_max(arr1, arr2, bcs)

    # print(f"arr1 = {arr1}")
    # print(f"arr2 = {arr2}")
    # print(f'max charge = {max_charge}')

    # 시간대로 돌기
    for t in range(M):
        # print(f'{t+1}초')
        # 움직임
        user1, user2 = move(user1, user2, people, t)

        #계산
        arr1 = get_possible_bcs(user1, bcs)
        arr2 = get_possible_bcs(user2, bcs)
        max_charge += calculate_max(arr1, arr2, bcs)

        # print(f"arr1 = {arr1}")
        # print(f"arr2 = {arr2}")
        # print(f'max charge = {max_charge}')
        # print()



    return max_charge
for test_case in range(1, T + 1):
   M, A = map(int, input().split())
   # 0 1 2 3 4
   # 정지 상 우 하 좌

   people = [list(map(int, input().split())) for _ in range(2)]
   # x, y, coverage, performance
   bcs = [list(map(int, input().split())) for _ in range(A)]
   user1 = (1,1)
   user2 = (10,10)

   result = solve(people, bcs, M, A, user1, user2)
   print(f"#{test_case} {result}")

