n = 3 ** 3
star = [["*"] * n for _ in range(n)]

# for i in star:
#     print("".join(i))

def blank(x, y, n):
    if n == 1:
        return
    else:
        # 1/3 ~ 2/3 공백 만들기
        for i in range(x + n//3, x + (n * 2)//3):
            for j in range(y + n//3, y + (n * 2)//3):
                star[i][j] = ' '
        # 재귀
        for i in range(x, x + n, n//3):
            for j in range(y, y + n, n//3):
                if star[i][j] == '*':
                    blank(i, j, n//3)

blank(0, 0, n)
for i in star:
    print("".join(i))
