import sys
from collections import deque
sys.stdin = open(r"스택\test.txt", "r")
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num = deque(num)
stack = deque()
stack.append(num.popleft())
result = [-1] * n

cnt = 0
while stack:
    if len(num) == 0 and len(stack) > 1:
        num = stack
        stack = deque()
        stack.append(num.popleft())
    if len(num) > 0 and len(stack) < 2:
        stack.append(num.popleft())
    while num and stack[0] > stack[-1]:
        stack.append(num.popleft())
    if stack[0] < stack[-1]:
        result[cnt] = stack[-1]
    stack.popleft()
    cnt += 1

for i in range(n):
    print(result[i], end=' ')
