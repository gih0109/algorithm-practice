import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    beachu = [[0] * m for _ in range(n)]
    check = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        beachu[b][a] = 1

    num = 0
    for i in range(n):
        for j in range(m):
            if beachu[i][j] == 1 and check[i][j] == 0:
                check[i][j] = 1
                que = deque()
                que.append((i, j))
                while que:
                    tmp = que.popleft()
                    for k in range(4):
                        x = tmp[0] + dx[k]
                        y = tmp[1] + dy[k]
                        if 0 <= x < n and 0 <= y < m:
                            if beachu[x][y] == 1 and check[x][y] == 0:
                                check[x][y] = 1
                                que.append((x, y))
                else:
                    num += 1
    print(num)
