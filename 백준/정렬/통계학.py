import sys
sys.stdin = open(r"정렬\test.txt", "r")
input = sys.stdin.readline

arr = []
plus_count, minus_count  = [0] * 4001, [0] * 4001
plus_sum, minus_sum = 0, 0

n = int(input())
for _ in range(n):
    num = int(input())
    arr.append(num)
    if num >= 0:
        plus_count[num] += 1
    else:
        minus_count[-num] += 1

# 산술평균
sum_val = sum(arr)
if sum_val >= 0:
    print(int(sum_val / n + 0.5))
elif sum_val < 0:
    print(int(sum_val / n - 0.5))

# 중앙값
arr.sort()
print(arr[int(n/2)])

# 최빈값
max_cnt = 0
max_list = []
for idx, val in enumerate(minus_count):
    if val > max_cnt:
        max_cnt = val
        max_list = [-idx]
    elif val == max_cnt:
        max_list.append(-idx)
for idx, val in enumerate(plus_count):
    if val > max_cnt:
        max_cnt = val
        max_list = [idx]
    elif val == max_cnt:
        max_list.append(idx)

if len(max_list) > 1:
    max_list.sort()
    print(max_list[1])
else:
    print(max_list[0])

# 범위
print(arr[-1] - arr[0])
