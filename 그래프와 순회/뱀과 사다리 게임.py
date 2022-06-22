import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
board = [0] * 101
for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

check = [-1] * 101
check[1] = 0
que = deque()
que.append(1)

while que:

    tmp = que.popleft()

    if tmp == 100:
        break

    for i in range(1, 7):
        a = tmp + i
        if 0 < a < 101 and check[a] == -1:
            if board[a] == 0:
                check[a] = check[tmp] + 1
                que.append(a)
            else:
                b = a
                while board[b]:
                    if check[board[b]] == -1:
                        check[board[b]] = check[tmp] + 1
                        b = board[b]
                        que.append(b)
                    else:
                        break

                check[a] = check[tmp] + 1
                que.append(a)

print(check[-1])