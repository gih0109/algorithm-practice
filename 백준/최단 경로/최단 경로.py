import sys
import heapq as hq
sys.stdin = open(r"백준\최단 경로\test.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
k = int(input().strip())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def search(k, V):
    visited = [INF] * (V+1)
    visited[k] = 0
    heap = []
    hq.heappush(heap, (0, k))

    while heap:
        now_w, now_p = hq.heappop(heap)

        for g in graph[now_p]:
            next_p, next_w = g[0], visited[now_p] + g[1]
            if next_w < visited[next_p]:
                visited[next_p] = next_w
                hq.heappush(heap, (next_w, next_p))

    for i in visited[1: ]:
        if i == INF:
            print("INF")
        else:
            print(i)

search(k, V)


