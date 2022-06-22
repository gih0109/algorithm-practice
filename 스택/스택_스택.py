import sys
sys.stdin = open(r"스택\test.txt", "r")
input = sys.stdin.readline

stack = []
n = int(input())
for _ in range(n):
    temp = str(input()).split()
    command = temp[0]

    if command == "push":
        stack.append(int(temp[1]))
    elif command == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif command == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)