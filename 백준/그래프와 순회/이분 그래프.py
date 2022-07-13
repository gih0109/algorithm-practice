import sys
from collections import deque
sys.stdin = open(r"백준\그래프와 순회\test.txt", "r")
input = sys.stdin.readline

def bfs(graph, check, start):
    que = deque()
    que.append(start)

    break_val = 0
    while que:
        now_p = que.popleft()

        for next_p in graph[now_p]:
            if check[next_p] == check[now_p]:
                return False
            
            elif check[next_p] == 0:
                if check[now_p] == 1:
                    check[next_p] = -1

                elif check[now_p] == -1:
                    check[next_p] = 1
            
                que.append(next_p)

    else:
        return True

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    check = [0] * (V + 1)

    result = True

    for i in range(1, V+1):
        if check[i] == 0:
            check[i] = 1
            result = bfs(graph, check, i)
            if result == False:
                print("NO")
                break
    else:
        print("YES")
            