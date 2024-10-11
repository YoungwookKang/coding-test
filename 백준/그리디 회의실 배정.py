"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""
n = int(input())
conferences = [list(map(int, input().split())) for _ in range(n)]
conferences.sort(key=lambda x: (x[1], x[0]))
count = 0
last_end_time = 0
for start, end in conferences:
    if start >= last_end_time:
        count += 1
        last_end_time = end
print(count)

