def solution(n):
    tri = [[0] * i for i in range(1, n+1)]
    
    # 좌표 초기화 
    x, y = -1, 0
    num = 1

    for i in range(n): # 방향
        for _ in range(i, n): # 좌표 구하기
            if i % 3 == 0: # 방향 아래
                x += 1
            
            elif i % 3 == 1: # 방향 오른쪽
                y += 1
            
            else:
                x -= 1
                y -= 1
            
            tri[x][y] = num
            num += 1

    answer = []
    for i in tri:
        answer += i

    return answer
    

if __name__ == "__main__":
    n = 5
    print(solution(n))