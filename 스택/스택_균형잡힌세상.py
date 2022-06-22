import sys
sys.stdin = open(r"스택\test.txt", "r")

while True:
    words = str(input())
    if words == '.':
        break
    else:
        stack = []
        for i in words:
            if i == '.':
                break
            elif i == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(i)
            elif i == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            elif i == '(' or i == '[':
                stack.append(i)
        if len(stack) > 0:
            print("no")
        else:
            print("yes")