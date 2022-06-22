import sys
sys.stdin = open(r"이분탐색\test.txt", "r")

n = int(input())
k = int(input())

# 이분탐색
lp = 0
rp = n ** 2
result = 0
while lp <= rp:
    midp = (lp + rp) // 2

    # 인덱스 계산
    idx = 0
    for i in range(1, n+1):
        tmp = midp//i
        if tmp == 0:
            break
        if tmp > n:
            tmp = n
        idx += tmp
    
    if idx >= k:
        result = midp
        rp = midp - 1
    else:
        lp = midp + 1

print(result)
