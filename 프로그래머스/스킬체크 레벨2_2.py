import sys
from collections import deque

def solution(n, wires):

    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(a, b, graph):
        que = deque()
        que.append(a)
        check = [0] * (n+1)
        check[a] = 1

        cnt = 0
        while que:
            tmp = que.popleft()
            for i in graph[tmp]:
                if check[i] == 0:
                    if tmp == a and i == b:
                        continue
                    check[i] = 1
                    que.append(i)
                    cnt += 1
        return cnt

    min_val = sys.maxsize
    for cut in wires:
        a, b = cut[0], cut[1]
        val =  abs(bfs(a, b, graph) - bfs(b, a, graph))
        if val < min_val:
            min_val = val

    return min_val

if __name__ == "__main__":
    n = 4
    wires = [[1,2],[2,3],[3,4]]
    print(solution(n, wires))