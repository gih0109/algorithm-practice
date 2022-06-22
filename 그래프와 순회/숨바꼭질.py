from collections import deque

n, k = 5, 17
time = [-1] * 100001
time[n] = 0
que = deque()
que.append(n)

while que:
    now_t = que.popleft()
    
    if now_t == k:
        break

    for next_t in (now_t-1, now_t+1, now_t*2):
        if 0 <= next_t <= 100000 and time[next_t] == -1:
            time[next_t] = time[now_t] + 1
            que.append(next_t)

print(time[k])