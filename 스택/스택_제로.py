import sys
sys.stdin = open(r"스택\test.txt", "r")
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)

print(sum(stack))