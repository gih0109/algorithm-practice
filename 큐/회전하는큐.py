import sys
from collections import deque
sys.stdin = open(r"큐\test.txt", "r")

n, m = map(int, input().split())
m_list = deque(list(map(int, input().split())))
que =  deque([i for i in range(1, n + 1)])

cnt = 0
while m_list:
    if m_list[0] == que[0]:
        m_list.popleft()
        que.popleft()
    else:
        point = que.index(m_list[0])
        if point >= len(que) - point:
            que.appendleft(que.pop())
        else:
            que.append(que.popleft())
        cnt += 1

print(cnt)

