import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

que = deque()
que.append(r)
visited[r] = 1

cnt = 2
while que:
    tmp = que.popleft()
    for i in graph[tmp]:
        if visited[i] == 0:
            visited[i] = cnt
            que.append(i)
            cnt += 1

print(visited)
for i in visited[1: ]:
    print(i)