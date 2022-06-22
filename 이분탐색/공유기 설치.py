import sys
sys.stdin = open(r"이분탐색\test.txt", "r")

n, c = map(int, input().split())
n_list = [int(input()) for _ in range(n)]
n_list.sort()

lp = 0
rp = n_list[-1]
result = 0
while lp <= rp:
    midp = (lp + rp) // 2

    cnt = 1
    idx = 0
    for i in range(1, len(n_list)):
        if n_list[i] - n_list[idx] >= midp:
            idx = i
            cnt += 1
    
    if cnt >= c:
        result = midp
        lp = midp + 1

    else:
        rp = midp - 1

print(result)
