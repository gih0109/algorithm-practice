def rotation(n, tri):
    result = [[0] * i for i in range(1, n+1)]
    num = n - 1
    
    for i in range(n):
        for j in range(len(tri[i])):
            result[i][j] = tri[n-1-j][n-1-num-j+i]

    return result

def solution(tri, direction):
    n = len(tri)
    answer = rotation(n, tri)
    
    if direction == 1: # 0: 시계방향 60도, 1: 반시계방향 60도
        answer = rotation(n, answer) # 반시계방향 60도 == 시계방향 120도 한번 더 돌린다

    return answer

if __name__ == "__main__":
    direction = 0 
    # tri = [[1], [2, 9], [3, 10, 8], [4, 5, 6, 7]]
    tri = [[1], [2, 12], [3, 13, 11], [4, 14, 15, 10], [5, 6, 7, 8, 9]]
    for i in tri:
        print(i)
    print()
    print(solution(tri, direction))
