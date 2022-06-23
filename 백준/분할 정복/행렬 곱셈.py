import sys
sys.stdin = open(r"분할 정복\test.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
matrix_1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrix_2 = [list(map(int, input().split())) for _ in range(m)]

result = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for a in range(m):
            result[i][j] += matrix_1[i][a] * matrix_2[a][j]

for row in result:
    for val in row:
        print(val, end=' ')
    print()