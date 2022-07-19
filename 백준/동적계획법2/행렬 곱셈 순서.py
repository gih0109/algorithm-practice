import sys
sys.stdin = open(r"백준\동적계획법2\test.txt", "r")
input = sys.stdin.readline

n = int(input())
matrix  = [list(map(int, input().split())) for _ in range(n)]
# sum_arr = [0] * n

dy = [[0] * n for _ in range(n)]

for i in range(1, n): # 몇번쨰 대각선 
    for j in range(n-i): # 대각선에서 몇 번째 열

        min_val = sys.maxsize
        for k in range(j, j+i):
            tmp = dy[j][k] + dy[k+1][i+j] + matrix[j][0] * matrix[k][1] * matrix[i+j][1]

            if tmp < min_val:
                min_val = tmp
        
        dy[j][j+i] = min_val

print(dy[0][-1])



