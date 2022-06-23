import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")
input = sys.stdin.readline

n = int(input())
m = int(input())
net = [list(map(int, input().split())) for _ in range(m)]

check = [0] * (n + 1)
check[1] = 1
que = deque()
que.append(1)

cnt = 0
while que:
    tmp = que.popleft()
    for j in net:
        if j[0] == tmp and check[j[1]] == 0:
            check[j[1]] = 1
            que.append(j[1])
            cnt += 1
        elif j[1] == tmp and check[j[0]] == 0:
            check[j[0]] = 1
            que.append(j[0])
            cnt += 1

print(cnt)