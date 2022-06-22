import sys
sys.stdin = open(r"input.txt", "r")

n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
coin_list.sort(reverse= True)
cnt = 0
for coin in coin_list:
    if k / coin >= 1:
        cnt += k // coin
        k = k % coin
print(cnt)