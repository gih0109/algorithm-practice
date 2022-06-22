import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def func():
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    board = [[-1] * l for _ in range(l)]

    que = deque()
    que.append(start)
    board[start[0]][start[1]] = 0

    while que:
        tmp = que.popleft()

        if tmp == end:
            break

        for i in range(8):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x < l and 0 <= y < l and board[x][y] == -1:
                board[x][y] = board[tmp[0]][tmp[1]] + 1
                que.append([x, y])

    print(board[end[0]][end[1]])

n = int(input())
for _ in range(n):
    func()


