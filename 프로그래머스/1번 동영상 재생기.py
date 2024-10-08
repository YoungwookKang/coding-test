def convert_to_str(temp):
    result = []
    minute = temp[0]
    minute = str(minute)
    sec = temp[1]
    sec = str(sec)
    if temp[0] < 10:
        minute = '0' + minute
        result.append(minute)
    else:
        result.append(minute)
    if temp[1] < 10:
        sec = '0' + sec
        result.append(sec)
    else:
        result.append(sec)

    real = result[0] + ":" + result[1]
    return real


def in_opening(pres, op_s, op_e):
    if op_s[0] == pres[0] == op_e[0]:
        if op_s[1] <= pres[1] <= op_e[1]:
            return op_e
    if op_s[0] == pres[0] < op_e[0]:
        if op_s[1] <= pres[1]:
            return op_e
    if op_s[0] < pres[0] == op_e[0]:
        if pres[1] <= op_e[1]:
            return op_e
    if op_s[0] < pres[0] < op_e[0]:
        return op_e
    return pres


def pr(pres):
    current_time = pres[0] * 60 + pres[1]
    if current_time - 10 <= 0:
        return [0, 0]
    else:
        current_time -= 10
        temp = []
        temp.append(current_time // 60)
        temp.append(current_time % 60)
        return temp


def nx(pres, video_length):
    current_time = pres[0] * 60 + pres[1]
    video_time = video_length[0] * 60 + video_length[1]
    if current_time + 10 >= video_time:
        return video_length
    else:
        current_time += 10
        temp = []
        temp.append(current_time // 60)
        temp.append(current_time % 60)
        return temp


def solution(video_len, pos, op_start, op_end, commands):
    open_start = [int(ele) for ele in op_start.split(":")]
    open_end = [int(ele) for ele in op_end.split(":")]
    curr = [int(ele) for ele in pos.split(":")]
    video_length = [int(ele) for ele in video_len.split(":")]

    for command in commands:
        curr = in_opening(curr, open_start, open_end)
        if command == "prev":
            curr = pr(curr)
        elif command == "next":
            curr = nx(curr, video_length)
        print(f'after command {curr}')
        curr = in_opening(curr, open_start, open_end)
        print(curr)

    answer = convert_to_str(curr)
    print(answer)
    return answer