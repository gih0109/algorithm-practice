import sys
sys.setrecursionlimit(10 ** 9)
sys.stdin = open(r"백준\test.txt", "r")
from collections import defaultdict
input = sys.stdin.readline

N, R, Q = map(int, input().split())
tree = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

size = [0] * (N + 1)
def dfs(a, tree):
    size[a] = 1
    for node in tree[a]:
        if size[node] == 0:
            dfs(node, tree)
            size[a] += size[node]

dfs(R, tree)

for _ in range(Q):
    U = int(input())
    print(size[U])