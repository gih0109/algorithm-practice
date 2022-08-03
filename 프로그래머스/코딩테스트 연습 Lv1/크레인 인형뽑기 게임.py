def solution(board, moves):
    # 스택
    stack = []
    cnt = 0
    
    for move in moves:
        # board 탐색
        tmp = 0
        for h in range(len(board)):
            if board[h][move-1] > 0:
                tmp = board[h][move-1]
                board[h][move-1] = 0
                break
                
        if tmp:
            if stack and tmp == stack[-1]:
                stack.pop()
                cnt += 2
            else:
                stack.append(tmp)
        
    return cnt