def solution(m, n, puddles):
    dy = [[0] * m for _ in range(n)]
    dy[0][0] = 1

    for i in range(n):
        for j in range(m):
            n_x, n_y = 0, 0
            if i == 0 and j == 0:
                continue
            if [j+1, i+1] in puddles:
                continue
            if i - 1 >= 0:
                n_x = dy[i-1][j]
            if j - 1 >= 0:
                n_y = dy[i][j-1]
            dy[i][j] = (n_x + n_y) % 1000000007
    
    return dy[-1][-1]

if __name__ == "__main__":
    m, n = 4, 3
    puddles = [[2, 2]]
    print(solution(m, n, puddles))
