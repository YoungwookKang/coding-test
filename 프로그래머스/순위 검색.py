from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    # 조건 조합을 키로 하고, 해당 조건을 만족하는 지원자의 점수를 저장
    board = defaultdict(list)

    for entry in info:
        language, job, hist, food, score = entry.split()
        score = int(score)
        conditions = [language, job, hist, food]

        # 모든 조건의 조합(16가지)을 생성
        for i in range(16):
            key = []
            for j in range(4):
                if i & (1 << j):
                    key.append(conditions[j])
                else:
                    key.append('-')
            key_str = ' '.join(key)
            board[key_str].append(score)
    print(board)
    # 각 조건 조합의 점수 리스트를 정렬
    for key in board:
        board[key].sort()

    answer = []

    for q in query:
        # ' and '을 공백으로 대체하고, 마지막에 점수 분리
        q = q.replace(' and ', ' ').split()
        key = ' '.join(q[:-1])
        score = int(q[-1])

        # 해당 조건 조합의 점수 리스트 조회
        if key in board:
            scores = board[key]
            # 이진 탐색을 통해 score 이상인 지원자 수 계산
            idx = bisect_left(scores, score)
            count = len(scores) - idx
            answer.append(count)
        else:
            # 조건을 만족하는 지원자가 없는 경우
            answer.append(0)

    return answer


# 테스트
if __name__ == '__main__':
    info = [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"
    ]

    query = [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"
    ]

    print(solution(info, query))  # [1, 1, 1, 1, 2, 4]
