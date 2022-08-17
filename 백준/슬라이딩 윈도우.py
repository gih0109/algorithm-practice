import sys
sys.stdin = open("백준/test.txt", "r")
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

# 슬라이딩 윈도우
point_1, point_2 = 0, X
sum_val = sum(arr[0:X])
max_val = sum_val
cnt = 1
for _ in range(X, len(arr)):
    sum_val = sum_val - arr[point_1] + arr[point_2]
    if sum_val > max_val:
        max_val = sum_val
        cnt = 1
    elif sum_val == max_val:
        cnt += 1
        
    point_1 += 1
    point_2 += 1

if max_val > 0:
    print(max_val)
    print(cnt)
else:
    print("SAD")