def dfs(arr, n, start, current, result):
    if len(current) == n:
        result.append(current.copy())
        return
    # 현재 인덱스부터 끝까지 탐색
    for i in range(start, len(arr)):
        current.append(arr[i])
        dfs(arr, n, i + 1, current, result)
        current.pop()
def generate_combinations(arr, n):
    result = []
    dfs(arr, n, 0, [], result)
    return result


def dfs_combinations(start, current, arr, result):
    # 모든 카테고리를 탐색했을 때
    if start == len(arr):
        if current:  # 최소 한 개의 의상을 선택했을 경우
            result.append(current.copy())
        return

    # 현재 카테고리의 모든 의상을 선택
    for cloth in arr[start]:
        current.append(cloth)
        dfs_combinations(start + 1, current, arr, result)
        current.pop()

    # 현재 카테고리에서 아무것도 선택하지 않음
    dfs_combinations(start + 1, current, arr, result)


def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        cloth_name, cloth_type = cloth
        if cloth_type in clothes_dict:
            clothes_dict[cloth_type].append(cloth_name)
        else:
            clothes_dict[cloth_type] = [cloth_name]

    arr = list(clothes_dict.values())

    result = []
    dfs_combinations(0, [], arr, result)

    # 모든 조합을 출력 (디버깅 용도)
    print(result)

    # 조합의 수 계산
    return len(result)


# 예시 사용
if __name__ == "__main__":
    phone_book = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 3  # 원하는 조합의 크기

    combinations = generate_combinations(phone_book, n)
    print(f"총 조합의 수: {len(combinations)}")
    for comb in combinations:
        print(comb)
