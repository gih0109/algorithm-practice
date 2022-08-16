import sys
import heapq as hq
sys.stdin = open(r"백준\최단 경로\test.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    nodes[a].append((c, b))
    nodes[b].append((c, a))
v1, v2 = map(int, input().split())

def func(node):
    visited = [INF] * (N + 1)
    visited[node] = 0
    heap = []
    hq.heappush(heap, (0, node))

    while heap:
        now_w, now_p = hq.heappop(heap)

        if visited[now_p] < now_w:
            continue

        for n in nodes[now_p]:
            next_w, next_p = visited[now_p] + n[0], n[1]
            
            if next_w < visited[next_p]:
                visited[next_p] = next_w
                hq.heappush(heap, (next_w, next_p))

    return visited

start_1 = func(1)
start_v1, start_v2 = func(v1), func(v2)

path_v1 = start_1[v1] + start_v1[v2] + start_v2[N]
parh_v2 = start_1[v2] + start_v2[v1] + start_v1[N]

result = min(path_v1, parh_v2)
print(result if result < INF else -1)