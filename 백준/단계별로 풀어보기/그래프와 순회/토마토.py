import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
result = -2

que = deque()
zero_val = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            zero_val += 1
        elif box[i][j] == 1:
            que.append((i, j))

if zero_val == 0:
    result = 0
else:
    cnt = 0
    while que:
        for i in range(len(que)):
            tmp = que.popleft()
            for i in range(4):
                x = tmp[0] + dx[i]
                y = tmp[1] + dy[i]
                if 0 <= x < n and 0 <= y < m:
                    if box[x][y] == 0:
                        box[x][y] = 1
                        que.append((x, y))
        cnt += 1

if result == 0:
    print(0)
else:
    break_val = 0
    for i in range(n):
        if break_val == 1:
            break
        for j in range(m):
            if box[i][j] == 0:
                print(-1)
                break_val = 1
                break
    else:
        print(cnt-1)
