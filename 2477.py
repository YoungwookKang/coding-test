
T = int(input())

def solve(a_list, b_list, k_list, k, a, b):
    answer = 0
    reception_result = [[] for _ in range(len(a_list))]
    reception_time = [0 for _ in range(len(a_list))]
    repair_result = [[] for _ in range(len(b_list))]
    repair_time = [0 for _ in range(len(b_list))]
    people = [[i+1, k_list[i]] for i in range(len(k_list))]
    after_reception = []
    # print(reception_time)
    # print(reception_result)
    for p in people:
        # print(f'사람 {p[0]}')
        min_desk = [0, 30000000]
        need_allocate = True
        for i in range(len(a_list)):
            if reception_time[i] <= p[1]:
                reception_time[i] = a_list[i] + p[1]
                reception_result[i].append(p[0])
                after_reception.append([p[0], a_list[i] + p[1], i])
                need_allocate = False
                break
            else:
                if min_desk[1] > reception_time[i]:
                    min_desk = [i, reception_time[i]]

        if need_allocate:
            reception_time[min_desk[0]] = min_desk[1] + a_list[min_desk[0]]
            reception_result[min_desk[0]].append(p[0])
            after_reception.append([p[0], min_desk[1] + a_list[min_desk[0]], min_desk[0]])
    #     print(reception_time)
    #     print(reception_result)
    #
    # print(reception_time)
    # print(reception_result)
    # print(after_reception)
    after_reception.sort(key=lambda x: (x[1], x[2]))
    # print(after_reception)
    # print(f'repair start')
    for p in after_reception:
        # print(f'사람 {p[0]}')
        min_desk = [0, 3000000]
        need_allocate = True
        for i in range(len(b_list)):
            if repair_time[i] <= p[1]:
                repair_time[i] = b_list[i] + p[1]
                repair_result[i].append(p[0])
                need_allocate = False
                break
            else:
                if min_desk[1] > repair_time[i]:
                    min_desk = [i, repair_time[i]]

        if need_allocate:
            repair_time[min_desk[0]] = min_desk[1] + b_list[min_desk[0]]
            repair_result[min_desk[0]].append(p[0])
        # print(repair_time)
        # print(repair_result)
    find = False
    intersection = []
    for i in reception_result[a-1]:
        for j in repair_result[b-1]:
            if i == j:
                find = True
                intersection.append(i)
    for ele in intersection:
        answer += ele



    if find:
        return answer
    else:
        return -1


for test_case in range(1, T + 1):
    n,m,k,a,b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    k_list = list(map(int, input().split()))

    result = solve(a_list,b_list,k_list, k, a, b)
    print(f'#{test_case} {result}')



