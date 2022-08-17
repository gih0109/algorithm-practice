import heapq as hq

def solution(places):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = []

    board = []

    def bfs(a, b, board): #다익스트라 bfs
        heap = []
        hq.heappush(heap, [0, a, b])
        visited = [[1000] * 5 for _ in range(5)]
        visited[a][b] = 0

        while heap:
            cur_sum, cur_x, cur_y = hq.heappop(heap)
            if cur_sum == 3:
                break
            for i in range(4):
                n_x = cur_x + dx[i]
                n_y = cur_y + dy[i]
                if 0 <= n_x < 5 and 0 <= n_y < 5:
                    if cur_sum + 1 < visited[n_x][n_y]:
                        if cur_sum < 2 and board[n_x][n_y] == "P":
                            return False
                        elif board[n_x][n_y] == "O":
                            hq.heappush(heap, [cur_sum+1, n_x, n_y])
        
        return True

    for i in range(5): # 5개 케이스
        board = []
        for j in range(5): # board 만들기
            tmp = list(map(str, places[i][j]))
            board.append(tmp)

        break_check = 0
        for k in range(5):
            if break_check == 1:
                break
            for l in range(5):
                if board[k][l] == "P":
                    if bfs(k, l, board) == False:
                        result.append(0)
                        break_check = 1
                        break
        if break_check == 0:
            result.append(1)

    return result


if __name__ == "__main__":
    places = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
        ]
    print(solution(places))