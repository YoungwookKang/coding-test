from collections import defaultdict
import heapq
"""
핵심은 dijkstra를 얼마나 조금 사용하냐, heap을 얼마나 조금 업데이트 하냐로 효율성을 높이는 거였음.
처음엔 명령어 400 때만 dijkstra를 계산하고 최솟값을 뽑으면 되지않나 했는데,
그냥 heap이랑 distances를 모두 전역변수로 놓고
처음 할당될 때 (명령어 100)와 start가 바뀔 때만 dijkstra를 사용해서 distance 업데이트해주고 heap 새로 세팅하면 됐음

새로운 상품이 추가될 때 (명령어 200)나 상품 지울 때 (명령어 300, 400)는 goods 딕셔너리에서 goods_id 를 지우고
나중에 여행상품 판매 (명령어 400)할 때 while 문 사용해서 heap 에서 유요한 값 찾을 때까지 pop하고 유요하면 break 하는 방식으로 
효율성있게 짤 수 있었음 
"""

def dijkstra(graph, start, n):
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0

    path = [(0, start)]

    while path:
        current_distance, current_node = heapq.heappop(path)
        # print(current_distance, current_node)
        if current_distance > distances[current_node]:
            continue

        for neighbor, w in graph[current_node]:
            temp_distance = current_distance + w
            if temp_distance < distances[neighbor]:
                distances[neighbor] = temp_distance
                heapq.heappush(path, (temp_distance, neighbor))
    return distances


q = int(input())
orders = [list(map(int, input().split())) for _ in range(q)]
n = orders[0][1]
graph = [[] for _ in range(n)]
start = 0
valid_distance = False
distances = [float('inf') for _ in range(n)]
heap = []
# 상품
goods = defaultdict(list)
for order in orders:
    # 코드트리 랜드 건설
    if order[0] == 100:
        n, m = order[1], order[2]
        for i in range(1, m + 1):
            u, v, w = order[3 * i], order[3 * i + 1], order[3 * i + 2]
            graph[u].append((v, w))
            graph[v].append((u, w))
        distances = dijkstra(graph, start, n)
        valid_distance = True
    # 여행 상품 생성
    elif order[0] == 200:
        goods_id, revenue, dest = order[1], order[2], order[3]
        goods[goods_id].append((revenue, dest))
        if distances[dest] <= revenue and distances[dest] <= 2000000:
            profit = revenue - distances[dest]
            heapq.heappush(heap, (-profit, goods_id))

    # 여행 상품 취소
    elif order[0] == 300:
        goods_id = order[1]
        if goods_id in goods:
            del goods[goods_id]

    # 최적의 여행 상품 판매
    elif order[0] == 400:
        while heap:
            neg_profit, goods_id = heapq.heappop(heap)
            if goods_id in goods:
                print(goods_id)
                del goods[goods_id]
                break
        else:
            print(-1)
        a = 0
    # 여행 상품의 출발지 변경
    elif order[0] == 500:
        start = order[1]
        distances = dijkstra(graph, start, n)
        # Rebuild heap
        heap = []
        for goods_id in goods:
            revenue, dest = goods[goods_id][0][0], goods[goods_id][0][1]
            if distances[dest] <= revenue and distances[dest] <= 2000000:
                profit = revenue - distances[dest]
                heapq.heappush(heap, (-profit, goods_id))
        heap_valid = True

