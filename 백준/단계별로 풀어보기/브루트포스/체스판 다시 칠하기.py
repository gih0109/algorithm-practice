import sys
sys.stdin = open("백준/단계별로 풀어보기/브루트포스/test.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(str, input())))
# print(board)

def func(a, b, board):
    w_cnt = 0 # w 로 시작해서 칠하는 횟수
    b_cnt = 0 # b 로 시작해서 칠하는 횟수
    for i in range(a, a+8):
        for j in range(b, b+8):
            if (i+j) % 2 == 0: # 짝수일 경우
                if board[i][j] == "W": # 합이 짝수인 인덱스가 W 일 경우
                    b_cnt += 1 
                else:
                    w_cnt += 1
            else: # 홀수일 경우
                if board[i][j] == "W":
                    w_cnt += 1
                else:
                    b_cnt += 1

    return min(w_cnt, b_cnt)

min_val = sys.maxsize
for i in range(n-7):
    for j in range(m-7):
        tmp =  func(i, j, board) 
        if tmp < min_val:
            min_val = tmp

print(min_val)