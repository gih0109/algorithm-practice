n = int(input())

board = [0] * n
result = 0

# 깊이우선탐색
def dfs(x):
    global result

    if x == n:
        result += 1
        return
    
    else:
        for y in range(n): # y 좌표 탐색
            board[x] = y
            # (x, y) 가 이전 queen 이 공격할 수 있는 위치인지 확인하기 위해 탐색
            for pre_x in range(x):
                pre_y = board[pre_x]

                if pre_y == y: # 같은 y 좌표인지 확인
                    break
                
                if abs(y - pre_y) == abs(x - pre_x): # 대각선인지 확인
                    break

            else:
                dfs(x+1)

dfs(0)
print(result)
            
