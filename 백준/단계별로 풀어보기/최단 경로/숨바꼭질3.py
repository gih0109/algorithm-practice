import sys
import heapq as hq
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())
# N, K = 5, 17

visited = [INF] * 100001
visited[N] = 0
heap = []
hq.heappush(heap, (0, N))

nodes = [(1, -1), (1, 1), (0, 2)]

while heap:
    now_w, now_p = hq.heappop(heap)

    if visited[now_p] < now_w:
        continue

    for i in nodes:
        next_w = visited[now_p] + i[0]
        if i[1] == 2:
            next_p = now_p * 2
        else:
            next_p = now_p + i[1]
        
        if 0 <= next_p <= 100000 and next_w < visited[next_p]:
            visited[next_p] = next_w
            hq.heappush(heap, (next_w, next_p))

print(visited[K])