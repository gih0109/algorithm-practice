import sys
from collections import deque
sys.stdin = open(r"큐\test.txt", "r")

que = deque()
n = int(input())
for _ in range(n):
    tmp = list(map(str, input().split()))
    if tmp[0] == "push":
        que.append(tmp[1])
    elif tmp[0] == "pop":
        if len(que) > 0:
            print(que.popleft())
        else:
            print(-1)
    elif tmp[0] == "size":
        print(len(que))
    elif tmp[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == "front":
        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
    elif tmp[0] == "back":
        if len(que) > 0:
            print(que[-1])
        else:
            print(-1)