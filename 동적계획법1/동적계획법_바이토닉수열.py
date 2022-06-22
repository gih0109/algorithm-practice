import sys
sys.stdin = open(r"동적계획법1\test.txt", "r")

n = int(input())
num = list(map(int, input().split()))
num.insert(0, 0)
num.append(0)
dy = [[0] * (n + 2) for _ in range(2)]
dy[0][1] = 1
dy[1][-2] = 1
result = 0

for i in range(1, n+1):
    max_val_1 = 0
    max_val_2 = 0
    for k in range(i-1, 0, -1):
        if num[k] < num[i] and dy[0][k] > max_val_1:
            max_val_1 = dy[0][k]
        dy[0][i] = max_val_1 + 1
    for l in range(n-i, n+1):
        if num[l] < num[n-i] and dy[1][l] > max_val_2:
            max_val_2 = dy[1][l]
        dy[1][n-i] = max_val_2 + 1

for i in range(len(dy[0])):
    if dy[0][i] + dy[1][i] > result:
        result = dy[0][i] + dy[1][i]

print(result - 1)
