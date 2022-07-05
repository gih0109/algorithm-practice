import sys
from collections import deque
sys.stdin = open(r"백준\그래프와 순회\test.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[-1] * m for _ in range(n)] for _ in range(2)]
visited[0][0][0] = 1

que = deque()
que.append((0, 0, 0)) # destroy, x, y

while que:
    destroy, now_x, now_y = que.popleft()

    if now_x == n-1 and now_y == m-1:
        print(visited[destroy][now_x][now_y])
        break

    for i in range(4):
        x = now_x + dx[i]
        y = now_y + dy[i]

        if 0 <= x < n and 0 <= y < m and visited[destroy][x][y] == -1:
            if board[x][y] == 0:
                visited[destroy][x][y] = visited[destroy][now_x][now_y] + 1
                que.append((destroy, x, y))

            if destroy == 0 and board[x][y] == 1:
                visited[1][x][y] = visited[0][now_x][now_y] + 1
                que.append((1, x, y))
else:
    print(-1)