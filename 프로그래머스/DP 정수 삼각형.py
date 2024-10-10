"""
아래서 위로 더하면서 dp 사용
"""
def solution(triangle):
    for i in range(len(triangle)-1, 0,-1):
        for j in range(len(triangle[i])-1):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
    answer = triangle[0][0]
    return answer