import sys
from collections import deque
sys.stdin = open(r"그래프와 순회\test.txt", "r")
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# DFS
dfs_visited = [0] * (n + 1)
dfs_visited[v] = 1
dfs_result = []

def dfs(x):
    global dfs_result, dfs_visited

    dfs_result.append(str(x))

    for num, val in enumerate(graph[x]):
        if val == 1 and dfs_visited[num] == 0:
            dfs_visited[num] = 1
            dfs(num)
    
# BFS
bfs_visited = [0] * (n + 1)
bfs_visited[v] = 1
bfs_que = deque([v])
bfs_result = []

while bfs_que:
    temp = bfs_que.popleft()
    bfs_result.append(str(temp))
    
    for num, val in enumerate(graph[temp]):
        if val == 1 and bfs_visited[num] == 0:
            bfs_visited[num] = 1
            bfs_que.append(num)


# DFS 값 출력
dfs(v)
print(" ".join(dfs_result))

# BFS 값 출력
print(" ".join(bfs_result))
