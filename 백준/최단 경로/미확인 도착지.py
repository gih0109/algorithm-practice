import sys
import heapq as hq
sys.stdin = open(r"백준\최단 경로\test.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

# 다익스트라 알고리즘 함수 정의
def func(graph, s):
    visited = [INF] * (n + 1)
    visited[s] = 0
    heap = []
    hq.heappush(heap, (0, s))

    while heap:
        now_w, now_p = hq.heappop(heap)
        
        if visited[now_p] < now_w:
            continue

        for g in graph[now_p]:
            next_w, next_p = visited[now_p] + g[0], g[1]

            if next_w < visited[next_p]:
                visited[next_p] = next_w
                hq.heappush(heap, (next_w, next_p))
    
    return visited


T = int(input())
for _ in range(T):
    n, m ,t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    t_list = [int(input()) for _ in range(t)]

    start_s, start_g, start_h = func(graph, s), func(graph, g), func(graph, h)
    result = []
    for i in t_list:
        if start_s[g] + start_g[h] + start_h[i] == start_s[i] or start_s[h] + start_h[g] + start_g[i] == start_s[i]:
            result.append(i)

    result.sort()
    print(*result)
