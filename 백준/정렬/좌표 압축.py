import sys
from collections import defaultdict
sys.stdin = open(r"정렬\test.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tmp = list(set(arr))
tmp.sort()

arr_dict = defaultdict(int)
cnt = 0
for num in tmp:
    arr_dict[num] = cnt
    cnt += 1

result = [0] * n
for idx, val in enumerate(arr):
    result[idx] = str(arr_dict[val])

print(" ".join(result))