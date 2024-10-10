from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
stack = deque()
answer = deque()
answer.append(-1)
stack.append(numbers[n - 1])
for i in range(n - 2, -1, -1):
    # print(f'{numbers[i]} ', end='')
    # print(stack)
    while stack:
        curr_number = stack.pop()
        if curr_number > numbers[i]:
            answer.append(curr_number)
            stack.append(curr_number)
            break
    else:
        answer.append(-1)
    stack.append(numbers[i])
answer.reverse()
print(" ".join(map(str, answer)))
