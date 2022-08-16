from collections import defaultdict, deque

def solution(n, edge):
    node = defaultdict(list)
    for a, b in edge:
        node[a].append(b)
        node[b].append(a)
        
    que = deque()
    que.append(1)
    visited = [-1] * (n+1)
    visited[1] = 0
    
    while que:
        cur_pos = que.popleft()
        for next_pos in node[cur_pos]:
            if visited[next_pos] == -1:
                visited[next_pos] = visited[cur_pos] + 1
                que.append(next_pos)
    
    max_val = max(visited)
    cnt = 0
    for i in visited:
        if i == max_val:
            cnt += 1
            
    return cnt