import sys
sys.stdin = open(r"분할 정복\test.txt", "r")

n = int(input())
tree = [list(map(int, input())) for _ in range(n)]

# for i in tree:
#     print(i)

result = ""

def quadtree(x, y, n):
    global result

    check = tree[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if tree[i][j] != check:
                result += "("
                quadtree(x, y, n//2)
                quadtree(x, y + n//2, n//2)
                quadtree(x + n//2, y, n//2)
                quadtree(x + n//2, y + n//2, n//2)
                result += ")"
                return
    else:
        if check == 0:
            result += "0"
        else:
            result += "1"

quadtree(0, 0, n)
print(result)