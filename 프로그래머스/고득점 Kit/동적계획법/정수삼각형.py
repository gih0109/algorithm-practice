def solution(triangle):
    dy = [[0] * (i+1) for i in range(len(triangle))]
    dy[0][0] = triangle[0][0]

    max_val = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if 0 <= j-1 and j < len(triangle[i-1]):
                dy[i][j] = max(dy[i-1][j-1], dy[i-1][j]) + triangle[i][j]
            elif 0 > j-1:
                dy[i][j] = dy[i-1][j] + triangle[i][j]
            elif j >= len(triangle[i-1]):
                dy[i][j] = dy[i-1][j-1] + triangle[i][j]
            
            if i == len(triangle) - 1:
                if dy[i][j] > max_val:
                    max_val = dy[i][j] 

    return max_val


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))
