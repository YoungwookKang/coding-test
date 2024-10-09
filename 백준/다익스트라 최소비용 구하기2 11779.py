import heapq

"""
1. 다익스트라 알고리즘이란?
다익스트라 알고리즘은 그래프에서 한 노드(출발점)에서 다른 모든 노드까지의 최단 경로를 찾는 알고리즘입니다. 특히, **그래프의 모든 간선 가중치가 비음수(non-negative)**일 때 사용됩니다.

다익스트라 알고리즘의 특징:
단일 출발점 최단 경로: 하나의 출발점에서 다른 모든 노드까지의 최단 경로를 찾습니다.
비음수 가중치: 모든 간선의 가중치가 0 이상이어야 합니다.
우선순위 큐 활용: 효율성을 높이기 위해 우선순위 큐(힙)를 사용합니다.
시간 복잡도: 우선순위 큐를 사용할 경우, 시간 복잡도는 O((V + E) log V)입니다. 여기서 V는 노드의 수, E는 간선의 수입니다.

2. 다익스트라 알고리즘을 사용하는 상황
다익스트라 알고리즘은 다음과 같은 상황에서 사용됩니다:

그래프 내의 최단 경로를 찾아야 할 때:

예: 도시 간 최소 비용의 버스 노선 찾기, 지도에서 두 지점 간 최단 거리 찾기 등.
그래프의 간선 가중치가 비음수일 때:

음수 간선이 존재하면 벨만-포드 알고리즘과 같은 다른 알고리즘을 사용해야 합니다.
단일 출발점에서 여러 도착점까지의 최단 경로를 구할 때:

예: 한 도시에서 여러 도시로의 최소 비용 경로 찾기.


3. 다익스트라 알고리즘의 작동 원리
다익스트라 알고리즘은 다음과 같은 단계로 작동합니다:

초기화:

모든 노드까지의 최단 거리를 무한대로 설정합니다.
출발점의 거리를 0으로 설정합니다.
우선순위 큐에 출발점을 추가합니다.
반복:

우선순위 큐에서 현재 거리가 가장 짧은 노드를 꺼냅니다.
이 노드를 기준으로 인접한 노드들의 최단 거리를 업데이트합니다.
업데이트된 노드를 우선순위 큐에 추가합니다.
종료:

우선순위 큐가 빌 때까지 반복합니다.
모든 노드까지의 최단 거리가 확정됩니다.
"""
def dijkstra_with_path(graph, start, n):
    distances = [float('inf') for _ in range(n+1)]
    distances[start] = 0
    previous_node = [0 for _ in range(n+1)]

    heap = [(0, start)]
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        # print(current_distance, current_node)
        if current_distance > distances[current_node]:
            continue

        for neighbor, w in graph[current_node]:
            temp_distance = current_distance + w
            if temp_distance < distances[neighbor]:
                distances[neighbor] = temp_distance
                previous_node[neighbor] = current_node
                heapq.heappush(heap, (temp_distance, neighbor))

    return distances, previous_node

def reconstruct_path(previous, start, end):
    temp_path = []
    curr = end
    while curr != start:
        temp_path.append(curr)
        curr = previous[curr]
    temp_path.append(start)
    temp_path.reverse()
    return temp_path

n = int(input())
edge = int(input())
buses = [list(map(int, input().split())) for _ in range(edge)]
start_node, end_node = map(int, input().split())


graph = [[] for _ in range(n + 1)]
for bus in buses:
    u, v, w = bus[0], bus[1], bus[2]
    graph[u].append((v, w))

distances, previous = dijkstra_with_path(graph, start_node, n)
# print(distances)
path = reconstruct_path(previous, start_node, end_node)

print(distances[end_node])
print(len(path))
print(' '.join(map(str, path)))




