import sys
sys.stdin = open(r"백준\test.txt", "r")
from collections import deque
# input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(str, input())))

for i in board:
    print(*i)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for x in range(R):
    for y in range(C):
        pass


