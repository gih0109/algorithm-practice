import sys
sys.stdin = open(r"동적계획법1\test.txt", "r")

n = int(input())
num = list(map(int, input().split()))
num.insert(0, 0)


result = 0
dy = [0] * (n + 1)
dy[1] = 1

for i in range(1, n+1):
    max_val = 0
    for j in range(i-1, 0, -1):
        if num[j] < num[i] and dy[j] > max_val:
            max_val = dy[j]
        dy[i] = max_val + 1

    if dy[i] > result:
        result = dy[i]

print(result)
