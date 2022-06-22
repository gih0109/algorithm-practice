import sys
sys.setrecursionlimit(10 ** 9)
sys.stdin = open(r"그래프와 순회\test.txt", "r")
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(a: int)-> None:
    global count
    visited[a] = count
    graph[a].sort(reverse = True)
    for b in graph[a]:
        if visited[b] == 0:
            count += 1
            dfs(b)

dfs(r)
for i in range(1, n+1):
    print(visited[i])