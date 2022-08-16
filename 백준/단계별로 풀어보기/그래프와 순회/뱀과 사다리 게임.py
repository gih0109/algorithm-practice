import sys
from collections import deque
sys.stdin = open(r"백준\그래프와 순회\test.txt", "r")
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
    now_p = que.popleft()

    if now_p == 100:
        break

    for i in range(1, 7):
        next_p = now_p + i
        
        if 0 < next_p < 101 and check[next_p] == -1:
            if board[next_p] != 0:
                next_p = board[next_p]

            if check[next_p] == -1:
                check[next_p] = check[now_p] + 1
                que.append(next_p)

print(check[-1])