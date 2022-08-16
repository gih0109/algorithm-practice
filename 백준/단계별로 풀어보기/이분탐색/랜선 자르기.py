import sys
sys.stdin = open(r"이분탐색\test.txt", "r")

k, n = map(int, input().split())
wire_list = [int(input()) for _ in range(k)]
print(k, n)
print(wire_list)

lp = 0
rp = 2 ** 31
length = 0

while lp <= rp:
    mid_p = (lp + rp) // 2
    
    cnt = 0
    for wire in wire_list:
        cnt += wire // mid_p

    if cnt >= n:
        length = mid_p
        lp = mid_p + 1
    
    else:
        rp = mid_p - 1

# result = 0
# while True:
#     cnt = 0
#     for wire in wire_list:
#         cnt += wire // length
#     if cnt < n:
#         break
#     elif cnt == n:
#         result = length
#         length += 1

print(length)