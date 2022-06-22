import sys
sys.stdin = open(r"C:\Users\gih54\OneDrive\백준\input.txt", "r")

t = int(input())
t_list = list(int(input()) for _ in range(t))

for n in t_list:
    if n < 2:
        if n == 0:
            print("1 0")
        if n == 1:
            print("0 1")
    else:
        check = [0] * (n + 1)
        check[1] = 1
        check[2] = 1
        for i in range(2, n + 1):
            check[i] = check[i-1] + check[i-2]
        print(check[-2], check[-1])