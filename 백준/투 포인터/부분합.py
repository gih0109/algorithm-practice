import sys
sys.stdin = open(r"백준\투 포인터\test.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

N, S = map(int, input().split())
arr = list(map(int, input().split()))

sum_val = 0
min_length = INF
left_p, right_p = 0, 0

while right_p < N:
    if sum_val >= S:
        min_length = min(min_length, right_p - left_p)
        sum_val -= arr[left_p]
        left_p += 1
            
    else:
        sum_val += arr[right_p]
        right_p += 1

print(min_length if min_length != INF else 0)