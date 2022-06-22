import sys
sys.stdin = open(r"동적계획법1\test.txt", "r")

n = int(input())
stair = [int(input()) for _ in range(n)]

if n == 1:
    print(stair[0])

elif n == 2:
    print(stair[0] + stair[1])

else:
    dy = [[0] * 3 for _ in range(n+1)]
    dy[1][1] = stair[0]
    dy[2] = [0, stair[1] + stair[0], stair[1]]

    for i in range(3, n+1):
        dy[i][1] = stair[i-1] + dy[i-1][2]
        dy[i][2] = stair[i-1] + max(dy[i-2])

    print(max(dy[-1]))