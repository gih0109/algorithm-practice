import sys
from collections import deque
sys.stdin = open(r"큐\test.txt", "r")

x = int(input())

for _ in range(x):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    que = deque([(pos, val) for pos, val in enumerate(n_list)])

    cnt = 0
    while que:
        now = que.popleft()
        if any(now[1] < q[1] for q in que):
            que.append(now)
        else:
            cnt += 1
            if now[0] == m:
                print(cnt)
