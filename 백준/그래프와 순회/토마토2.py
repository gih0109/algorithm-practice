import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

que = deque()
zero_val = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                zero_val += 1
            elif box[i][j][k] == 1:
                que.append((i, j, k))

result = None
if zero_val == 0:
    result = 0
else:
    cnt = 0
    while que:
        for _ in range(len(que)):
            tmp = que.popleft()
            for i in range(6):
                z = tmp[0] + dz[i]
                y = tmp[1] + dy[i]
                x = tmp[2] + dx[i]
                if 0 <= z < h and 0 <= y < n and 0 <= x < m:
                    if box[z][y][x] == 0:
                        box[z][y][x] = 1
                        que.append((z, y, x))
        cnt += 1

if result == 0:
    print(result)
else:
    break_val_1 = 0
    break_val_2 = 0
    for height in box:
        if break_val_1 == 1:
            break
        for row in height:
            if break_val_2 == 1:
                break_val_1 = 1
                break
            for num in row:
                if num == 0:
                    break_val_2 = 1
                    result = -1
                    break
    if result == -1:
        print(result)
    else:
        print(cnt-1)
