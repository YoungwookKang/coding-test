n = int(input())
towers = list(map(int, input().split()))

answer = [0]
stack  = [(towers[0],0)]
for i in range(1,n):
    curr_height, curr_idx = towers[i], i
    temp = []
    get_value = 0
    find = False
    # print(stack)
    while stack:
        tallest_tower, tallest_tower_idx = stack.pop()
        if tallest_tower > curr_height:
            get_value = tallest_tower_idx
            stack.append((tallest_tower,tallest_tower_idx))
            find = True
            break
    if find:
        answer.append(get_value + 1)
    else:
        answer.append(0)
    stack.append((curr_height,curr_idx))


print(' '.join(map(str,answer)))
