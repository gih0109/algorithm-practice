import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

que = deque()
que.append((0, 0))
check[0][0] = 1

while que:
    if check[-1][-1] != 0:
        break
    tmp = que.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x < n and 0 <= y < m:
            if maze[x][y] == 1 and check[x][y] == 0:
                check[x][y] = check[tmp[0]][tmp[1]] + 1
                que.append((x, y))

print(check[-1][-1])
        