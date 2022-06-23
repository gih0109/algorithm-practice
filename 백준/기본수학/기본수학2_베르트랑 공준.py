import sys
sys.stdin = open(r"C:\Users\gih54\OneDrive\백준\input.txt", "r")

while True:
    n = int(input())
    if n == 0:
        break
    else:
        n1 = n
        n2 = n * 2
        check = [0] * (n2 + 1)
        cnt = 0
        for i in range(2, n2 + 1):
            if check[i] == 0:
                if i > n1:
                    cnt += 1
                for j in range(i, n2+1, i):
                    check[j] = 1
        print(cnt)