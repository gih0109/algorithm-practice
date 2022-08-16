import sys
sys.stdin = open(r"분할 정복\test.txt", "r")

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# for i in paper:
#     print(i)

cnt_1, cnt_0, cnt_m1 = 0, 0, 0

def tree(x, y, n):
    global cnt_0, cnt_1, cnt_m1

    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != check:

                for k in range(x, x + n, n//3):
                    for l in range(y, y + n, n//3):
                        tree(k, l, n//3)
                return
    else:
        if check == 0:
            cnt_0 += 1
        elif check == 1:
            cnt_1 += 1
        else:
            cnt_m1 += 1

tree(0, 0, n)
print(cnt_m1)
print(cnt_0)
print(cnt_1)