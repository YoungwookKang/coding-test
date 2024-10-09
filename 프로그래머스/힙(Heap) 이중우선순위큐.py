import heapq

"""
이중 우선순위 큐
접근 방법
이중 우선순위 큐를 효율적으로 구현하기 위해 두 개의 힙을 사용하는 방법을 권장합니다:

최소 힙 (Min Heap): 큐에서 최솟값을 빠르게 추출하기 위해 사용.
최대 힙 (Max Heap): 큐에서 최댓값을 빠르게 추출하기 위해 사용.
그러나 단순히 두 개의 힙을 사용하는 것만으로는 동기화 문제가 발생합니다. 동일한 요소가 두 힙에 모두 존재해야 하지만, 하나의 힙에서 삭제되었을 때 다른 힙에서도 이를 반영해야 합니다. 이를 해결하기 위해 **유효성 검사 (Validity Check)**를 추가해야 합니다.

유효성 검사를 위한 방법:
중복된 요소를 추적: 각 요소에 고유한 ID를 부여하여 두 힙에서 동일한 요소를 식별할 수 있도록 합니다.
삭제된 요소를 추적: 삭제된 요소를 기록하여, 힙에서 요소를 추출할 때 유효한지 확인합니다.
이를 위해 **딕셔너리 (Dictionary)**를 사용하여 각 요소의 유효성을 관리합니다.

구현 단계
데이터 정렬:

최소 힙과 최대 힙을 별도로 유지하기 위해, 최소 힙은 그대로 사용하고 최대 힙은 요소를 음수로 저장하여 최소 힙을 최대 힙처럼 동작하게 합니다.
삽입 연산 (I 숫자):

최소 힙과 최대 힙에 모두 요소를 삽입.
각 요소에 고유한 ID를 부여하고, 딕셔너리에 이를 기록.
삭제 연산 (D 1 또는 D -1):

D 1: 최대 힙에서 최댓값을 추출하고, 해당 요소의 유효성을 제거.
D -1: 최소 힙에서 최솟값을 추출하고, 해당 요소의 유효성을 제거.
힙에서 요소를 추출할 때, 유효하지 않은 요소는 무시하고 다음 요소를 확인.
최종 결과 도출:

큐가 비어있으면 [0, 0].
비어있지 않으면, 최소 힙과 최대 힙에서 각각 최솟값과 최댓값을 추출.

"""


def solution(operations):
    min_heap = []
    max_heap = []
    entry_finder = {}
    idx = 0
    for operation in operations:
        cmd, str_num = operation.split(" ")
        num = int(str_num)
        if cmd == "I":
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            entry_finder[idx] = True
            idx += 1
        else:
            if num == -1:
                while min_heap:
                    min_num, min_idx = heapq.heappop(min_heap)
                    if min_idx in entry_finder and entry_finder[min_idx]:
                        entry_finder[min_idx] = False
                        break
            else:

                while max_heap:
                    max_num, max_idx = heapq.heappop(max_heap)
                    if max_idx in entry_finder and entry_finder[max_idx]:
                        entry_finder[max_idx] = False
                        break

    # print(min_heap)
    # print(max_heap)

    valid_elements = []
    for value, id in min_heap:
        if id in entry_finder and entry_finder[id]:
            valid_elements.append(value)

    if not valid_elements:
        return [0, 0]
    else:
        return [max(valid_elements), min(valid_elements)]