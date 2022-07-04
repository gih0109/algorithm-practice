import sys
sys.stdin = open(r"백준\스택\test.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []

result = [-1] * n

for idx in range(n):
    while stack and stack[-1][0] < arr[idx]:
        tmp_val, tmp_idx = stack.pop()
        result[tmp_idx] = arr[idx]
    stack.append((arr[idx], idx))

print(*result)