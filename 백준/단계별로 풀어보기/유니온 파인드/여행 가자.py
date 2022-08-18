import sys
sys.setrecursionlimit(10 ** 9)
sys.stdin = open("백준/단계별로 풀어보기/유니온 파인드/test.txt", "r")
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, N+1):
    node_list = list(map(int, input().split()))
    for j in range(1, N+1):
        if i != j and node_list[j-1] == 1:
            union_parent(i, j)

cities = list(map(int, input().split()))
val = parent[cities[0]]
answer = "YES"
for i in cities[1:]:
    if parent[i] != val:
        answer = "NO"
        break
print(answer)