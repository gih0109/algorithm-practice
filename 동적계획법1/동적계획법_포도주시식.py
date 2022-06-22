import sys
sys.stdin = open(r"동적계획법1\test.txt", "r")

n = int(input())
wine_list = [int(input()) for _ in range(n)]
wine_list.insert(0, 0)

dy = [[0] * 3 for _ in range(n+1)]
dy[1] = [0, wine_list[1], 0]
dy[2] = [0, wine_list[1] + wine_list[2], wine_list[2]]

if n == 1:
    print(dy[1][1])
elif n == 2:
    print(dy[2][1])
else:
    max_val = 0
    for i in range(3, n + 1):
        dy[i][1] = wine_list[i] + dy[i-1][2]
        dy[i][2] = wine_list[i] + max(dy[i-2])
        tmp = max(dy[i][1], dy[i][2])
        if tmp > max_val:
            max_val = tmp

print(max_val)
