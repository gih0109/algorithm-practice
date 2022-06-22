import sys
sys.stdin = open(r"input.txt", "r")

n = int(input())
line_list = list(map(int, input().split()))
line_list.sort()
answer = 0
time = 0
for i in line_list:
    time += i
    answer += time
print(answer)