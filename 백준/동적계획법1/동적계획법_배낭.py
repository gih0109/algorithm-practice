import sys
sys.stdin = open(r"동적계획법1\test.txt", "r")

n, k = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

dy = [0] * (k + 1)
result = 0
for weight, val in n_list:
    for idx in range(k, weight - 1, -1):
        dy[idx] = max(dy[idx], dy[idx - weight] + val)
        if dy[idx] > result:
            result = dy[idx]

print(result)