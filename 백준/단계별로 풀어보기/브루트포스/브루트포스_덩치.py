import sys
sys.stdin = open(r"브루트포스\test.txt", "r")

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
# print(n_list)
result = []

for i in range(n):
    cnt = 0
    for j in range(n):
        if n_list[i][0] < n_list[j][0] and n_list[i][1] < n_list[j][1]:
            cnt += 1
    result.append(cnt+1)

for i in result:
    print(i, end=' ')
