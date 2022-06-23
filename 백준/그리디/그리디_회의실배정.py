import sys
sys.stdin = open(r"input.txt", "r")

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

print(n_list)
n_list.sort(key= lambda x: (x[1], x[0]))
print(n_list)

cnt = 1
end = n_list[0][1]
for i in n_list[1 : ]:
    if i[0] >= end:
        end = i[1]
        cnt += 1
print(cnt)