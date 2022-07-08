def solution(m, n, puddles):
    dy = [[0] * m for _ in range(n)]
    
    dy[0][0] = 1

    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                continue
            if i == 0 and j == 0:
                dy[i][j] = 1
            elif i == 0:
                dy[i][j] = dy[i][j-1]
            elif j == 0:
                dy[i][j] = dy[i-1][j]
            else:
                dy[i][j] = (dy[i-1][j] + dy[i][j-1]) % 1000000007

    return dy[-1][-1]

if __name__ == "__main__":
    m, n = 4, 3
    puddles = [[2, 2]]
    print(solution(m, n, puddles))
