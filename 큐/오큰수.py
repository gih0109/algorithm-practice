import sys
from collections import deque
sys.stdin = open(r"큐\test.txt", "r")
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
stack = num[ : :-1]
num = deque(num)
stack.pop()
result = ""

cnt = 0
for idx in range(n - 1):
    now_p = num[idx]

    if n - idx < len(stack) + 1:
        stack.pop()

    if len(stack) > 0 and num[idx] >= max(stack):
        result += "-1 "
        continue
    else:
        while stack[-1] < now_p:
            stack.pop()
        result += str(stack[-1])
        result += " "

result += "-1"
print(result)