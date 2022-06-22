import sys
sys.stdin = open(r"동적계획법\test.txt", "r")

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
print(n)
print(cost)
dy = [[0] * 3 for _ in range(n)]
dy[0] = cost[0]

dy[1][0] = cost[1][0] + min(cost[0][1], cost[0][2])
dy[1][1] = cost[1][1] + min(cost[0][0], cost[0][2])
dy[1][2] = cost[1][2] + min(cost[0][0], cost[0][1])

for i in range(2, n):
    dy[i][0] = cost[i][0] + min(dy[i-1][1], dy[i-1][2])
    dy[i][1] = cost[i][1] + min(dy[i-1][0], dy[i-1][2])
    dy[i][2] = cost[i][2] + min(dy[i-1][0], dy[i-1][1])

print(min(dy[-1]))