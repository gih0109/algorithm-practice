import sys
from collections import defaultdict, deque

# 넓이우선탐색
def bfs(a, b, wire_node):
    que = deque()
    que.append(a)
    visited = [0] * (n + 1)
    visited[a] = 1
    
    cnt = 0
    while que:
        tmp = que.popleft()
        for next_wire in wire_node[tmp]:
            if tmp == a and next_wire == b:
                continue
            if visited[next_wire] == 0:
                visited[next_wire] = 1
                que.append(next_wire)
                cnt += 1
                
    return cnt
                    
def solution(n, wires):
    # 전력망 노드 생성
    wire_node = defaultdict(list)
    for a, b in wires:
        wire_node[a].append(b)
        wire_node[b].append(a)
        
    # 전력망 끊기 순환
    min_val = sys.maxsize # 최소값 초기화
    for wire in wires:
        cut1, cut2 = wire
        val = abs(bfs(cut1, cut2, wire_node) - bfs(cut2, cut1, wire_node))
        if val < min_val:
            min_val = val
    
    return min_val


if __name__ == "__main__":
    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    print(solution(n, wires))