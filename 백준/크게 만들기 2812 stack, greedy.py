"""
stack을 사용해서 앞에서부터 하나씩 스택에 넣다가 그 값이 스택의 값보다 크면 스택을 팝하는 식으로
매 순간 최고의 값을 구하는 그리디 알고리즘

"""

def make_largest_number(n, k, number):
    stack = []
    to_remove = k
    for num in number:
        while stack and to_remove > 0 and stack[-1] < num:
            stack.pop()
            to_remove -= 1
        stack.append(num)

    stack = stack[:len(stack)-to_remove]
    return "".join(map(str,stack))


n, k = map(int, input().split())
str_number = input()
int_number = int(str_number)

result = make_largest_number(n, k, str_number)
print(result)