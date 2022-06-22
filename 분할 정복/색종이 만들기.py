import sys
sys.stdin = open(r"분할 정복\test.txt", "r")

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# print(n)
# print(paper)

sum_white = 0
sum_blue = 0

def tree(x, y, n):
    global sum_blue, sum_white
    check = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                tree(x, y, n//2)
                tree(x, y + n//2, n//2)
                tree(x + n//2, y, n//2)
                tree(x + n//2, y + n//2, n//2)
                return
            
    else:
        if check == 1:
            sum_blue += 1
        else:
            sum_white += 1

tree(0, 0, n)
print(sum_white)
print(sum_blue)

