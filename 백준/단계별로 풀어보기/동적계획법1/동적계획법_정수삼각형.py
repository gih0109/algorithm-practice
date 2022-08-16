import sys
sys.stdin = open(r"동적계획법1\test.txt", "r")

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

dy = []
dy.append(tri[0])

if n == 1:
    print(dy[0][0])

else:
    for i in range(1, n):
        dy_temp = [0] * len(tri[i])
        for j in range(len(tri[i])):
            if j == 0:
                dy_temp[j] = dy[i-1][j] + tri[i][j]
            elif j == len(tri[i]) - 1:
                dy_temp[j] = dy[i-1][-1] + tri[i][j]
            else:
                dy_temp[j] = max(dy[i-1][j], dy[i-1][j-1]) + tri[i][j]
        dy.append(dy_temp)

    print(max(dy[-1]))

    