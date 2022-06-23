import sys
sys.stdin = open(r"누적 합\test.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (n+1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))
sum_arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_arr[i][j] = sum_arr[i][j-1] + arr[i][j] 

for i in range(1, n+1):
    for j in range(1, n+1):
            sum_arr[i][j] += sum_arr[i-1][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1])

