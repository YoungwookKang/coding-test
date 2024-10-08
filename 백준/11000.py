import heapq
n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
lectures.sort(key=lambda x: x[0])

max_value = 0

heap = []

for lecture in lectures:
    start_t, end_t = lecture[0], lecture[1]
    if heap and start_t >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, end_t)
print(len(heap))