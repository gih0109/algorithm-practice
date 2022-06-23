import sys
sys.stdin = open(r"스택\test.txt", "r")

n = int(input())

for _ in range(n):
    stack = []
    tmp = str(input())
    for i in tmp:
        if len(stack) > 0 and stack[-1] == '(' and i == ")":
            stack.pop()
        else:
            stack.append(i)
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")