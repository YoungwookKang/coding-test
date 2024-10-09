import heapq


def solution(scoville, K):
    heap = []

    for food in scoville:
        heapq.heappush(heap, (food))

    cnt = 0
    while heap[0] >= K:
        food_1 = heapq.heappop(heap)
        food_2 = heapq.heappop(heap)
        new_scoville = food_1 + (food_2 * 2)
        heapq.heappush(heap, new_scoville)
        cnt += 1
    return cnt