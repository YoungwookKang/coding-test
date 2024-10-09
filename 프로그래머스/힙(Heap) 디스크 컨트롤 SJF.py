import heapq

"""
Shortest Job First (SJF) 알고리즘

Shortest Job First (SJF) 알고리즘은 현재 실행 가능한 작업들 중에서 소요 시간이 가장 짧은 작업을 먼저 처리하는 전략입니다. 이 접근 방식은 평균 대기 시간을 최소화하는 데 효과적입니다.
"""


def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    heap = []
    current_time = 0
    total_time = 0
    idx = 0
    n = len(jobs)
    while idx < n or heap:
        # print(f"idx = {idx}, heap = {heap}")
        while idx < n and current_time >= jobs[idx][0]:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if heap:
            duration, start_time = heapq.heappop(heap)
            current_time += duration
            total_time += current_time - start_time
        else:
            if idx < n:
                current_time = jobs[idx][0]

    return total_time // n

