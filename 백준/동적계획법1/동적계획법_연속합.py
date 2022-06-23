import sys
sys.stdin = open(r"동적계획법1\test.txt", "r")

n = int(input())
num = list(map(int, input().split()))
num.insert(0, 0)

dy = [0] * (n + 1)
dy[1] = num[1]
result = -1001
for i in range(1, n+1):
    if dy[i-1] >= 0:
        dy[i] = num[i] + dy[i-1]
    else:
        dy[i] = num[i]
    if dy[i] > result:
        result = dy[i]

print(result)
