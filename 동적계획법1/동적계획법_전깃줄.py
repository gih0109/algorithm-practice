import sys
sys.stdin = open(r"동적계획법1\test.txt", "r")
input = sys.stdin.readline

n = int(input())
wires = [list(map(int, input().split())) for _ in range(n)]
num = [i[0] for i in sorted(wires, key= lambda x: x[1])]
num.insert(0, 0)

dy = [0] * (n + 1)
dy[1] = 1
result = 0

for i in range(1, n+1):
    max_val = 0
    for j in range(i-1, 0, -1):
        if num[j] < num[i] and dy[j] > max_val:
            max_val = dy[j]
    dy[i] = max_val + 1
    if dy[i] > result:
        result = dy[i]

print(n - result)
