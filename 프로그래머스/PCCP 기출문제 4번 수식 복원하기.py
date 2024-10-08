def trans(_num, _i):
    trans_num = 0
    cnt = 0
    while _num > 0:
        c = _num % 10
        if c >= _i:
            return False, 0
        trans_num += c * (_i ** cnt)
        _num = _num // 10
        cnt += 1
    return True, trans_num


def reverse_trans(_num, _i):
    trans_num = 0
    cnt = 0
    while _num > 0:
        c = _num % _i
        trans_num += c * (10 ** cnt)
        _num = _num // _i
        cnt += 1
    return trans_num


def find_value(v1, op, v2, r):
    if op == "+":
        if v1 + v2 == r:
            return True,
        else:
            return False
    if op == "-":
        if v1 - v2 == r:
            return True
        else:
            return False


def find_range(val1, oper, val2, right, i):
    can_do, trans_val1 = trans(val1, i)
    if not can_do:
        return False
    can_do, trans_val2 = trans(val2, i)
    if not can_do:
        return False
    can_do, trans_result = trans(right, i)
    if not can_do:
        return False

    return find_value(trans_val1, oper, trans_val2, trans_result)


def solve(p1_val1, p1_val2, p2_val1, p2_val2, opera, p1, p2):
    if opera == "+":
        total = p1_val1 + p1_val2
        if reverse_trans(total, p1) == reverse_trans((p2_val1 + p2_val2), p2):
            return str(reverse_trans(total, p1))
        else:
            return "?"
    else:
        total = p1_val1 - p1_val2
        if reverse_trans(total, p1) == reverse_trans((p2_val1 - p2_val2), p2):
            return str(reverse_trans(total, p1))
        else:
            return "?"


def final_check(ans, can_calculate):
    v_1, opera, v_2 = ans[0], ans[1], ans[2]
    p1, p2 = can_calculate[0], can_calculate[-1]
    _, p1_val1 = trans(int(v_1), p1)
    _, p1_val2 = trans(int(v_2), p1)

    _, p2_val1 = trans(int(v_1), p2)
    _, p2_val2 = trans(int(v_2), p2)

    val = solve(p1_val1, p1_val2, p2_val1, p2_val2, opera, p1, p2)
    return v_1 + " " + opera + " " + v_2 + " = " + val


def solution(expressions):
    answer = []
    can_calculate = [2, 3, 4, 5, 6, 7, 8, 9]
    for expression in expressions:
        print(expression)
        left, right = expression.split(" = ")
        val1, oper, val2 = left.split(" ")
        if right == "X":
            answer.append((val1, oper, val2, right))
            for i in range(2, 10):
                b = True
                b, _ = trans(int(val1), i)
                if not b:
                    if i in can_calculate:
                        can_calculate.remove(i)
                b, _ = trans(int(val2), i)
                if not b:
                    if i in can_calculate:
                        can_calculate.remove(i)

        else:
            for i in range(2, 10):
                # print(f"{int(val1),oper,int(val2),int(right), i}")
                a = find_range(int(val1), oper, int(val2), int(right), i)
                if not a:
                    if i in can_calculate:
                        can_calculate.remove(i)

    real_answer = []
    for ans in answer:
        real_answer.append(final_check(ans, can_calculate))
    # print(f'경우의 수 {can_calculate}')
    # print(real_answer)
    return real_answer

