import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")

n = int(input())
n_map = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

num = 1
check_map = [[0] * n for _ in range(n)]
result = []

# search 1
for row in range(n):
    for col in range(n):
        if n_map[row][col] == 1 and check_map[row][col] == 0:

            # BFS
            cnt = 1
            que = deque()
            que.append((row, col))
            check_map[row][col] = num

            while que:
                tmp = que.popleft()

                for i in range(4):
                    tmp_x = tmp[0] + dx[i]
                    tmp_y = tmp[1] + dy[i]

                    if 0 <= tmp_x < n and 0 <= tmp_y < n:
                        if n_map[tmp_x][tmp_y] == 1 and check_map[tmp_x][tmp_y] == 0:
                            cnt += 1
                            check_map[tmp_x][tmp_y] = num
                            que.append((tmp_x, tmp_y))
            else:
                result.append(cnt)
                num += 1

result.sort()
print(num - 1)
for val in result:
    print(val)
