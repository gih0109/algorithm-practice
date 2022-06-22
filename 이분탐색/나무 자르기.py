import sys
sys.stdin = open(r"이분탐색\test.txt", "r")

n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

lp = 0
rp = 1000000001
result = 0

while lp <= rp:
    mid_p = (lp + rp) // 2

    length = 0
    for i in tree_list:
        if i > mid_p:
            length += i - mid_p

    if length >= m:
        result = mid_p
        lp = mid_p + 1
    
    else:
        rp = mid_p - 1

print(result)