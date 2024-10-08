n = int(input())
apt = []
for i in range(n):
    apt.append(int(input()))

answer = 0
stack = [(apt[0], 0)]
for i in range(1, n):
    curr_height, curr_idx = apt[i], i
    temp = []
    get_value = 0
    find = False
    while stack:
        tallest_tower, tallest_tower_idx = stack.pop()
        if tallest_tower > curr_height:
            get_value = tallest_tower_idx
            stack.append((tallest_tower, tallest_tower_idx))
            find = True
            break
    if find:
        answer += len(stack)

    stack.append((curr_height, curr_idx))

print(answer)
