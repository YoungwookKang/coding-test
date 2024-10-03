def solve(level, diffs, times, limit):
    cnt = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            cnt += times[i]
        else:
            fail = diffs[i] - level
            cnt += fail * (times[i] + times[i - 1]) + times[i]

    if cnt <= limit:
        return True
    else:
        return False


def solution(diffs, times, limit):
    right = 100000
    left = 1
    while left < right:
        curr = (right + left) // 2
        can_do = solve(curr, diffs, times, limit)
        if can_do:
            right = curr
        else:
            left = curr + 1
    answer = left
    return answer