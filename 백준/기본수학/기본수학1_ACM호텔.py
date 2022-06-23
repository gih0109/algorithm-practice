import sys
sys.stdin = open(r"기본수학\test.txt", "r")

n = int(input())

for _ in range(n):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print((n // h) * 100 + h)
    else:
        print((n % h) * 100 + (n // h) + 1)