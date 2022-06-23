import sys
sys.stdin = open(r"스택\test.txt", "r")
input = sys.stdin.readline


n = int(input())
num_list = [int(input()) for _ in range(n)]
# print(num_list)

result = []
stack = []
pointer = 0
for i in range(1, n + 1):
    stack.append(i)
    result.append("+")
    while len(stack) > 0 and stack[-1] == num_list[pointer]:
        stack.pop()
        result.append("-")
        pointer += 1

if len(stack) > 0:
    print("NO")
else:
    for i in result:
        print(i)