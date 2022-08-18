from collections import deque

def solution(priorities, location):
    p_que = deque(priorities)
    l_que = deque([i for i in range(len(priorities))])
    
    cnt = 0
    while True:
        if p_que[0] == max(p_que):
            cnt += 1
            if l_que[0] == location:
                return cnt
            p_que.popleft()
            l_que.popleft()
        elif p_que[0] < max(p_que):
            p_que.append(p_que.popleft())
            l_que.append(l_que.popleft())
    