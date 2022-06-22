import sys
from collections import deque
sys.stdin = open(r"큐\test.txt", "r")

n = int(input())

que = deque()

for _ in range(n):
    tmp = list(map(str, input().split()))

    if tmp[0] == "push_front":
        que.appendleft(int(tmp[1]))
    elif tmp[0] == "push_back":
        que.append(int(tmp[1]))
    elif tmp[0] == "pop_front":
        if len(que) > 0:
            print(que.popleft())
        else:
            print(-1)
    elif tmp[0] == "pop_back":
        if len(que) > 0:
            print(que.pop())
        else:
            print(-1)
    elif tmp[0] == "size":
        print(len(que))
    elif tmp[0] == "empty":
        if len(que) > 0:
            print(0)
        else:
            print(1)
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
