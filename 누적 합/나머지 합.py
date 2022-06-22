import sys
sys.stdin = open(r"누적 합\test.txt", "r")

n, m = map(int, input().split())
arr = list(map(int,input().split()))

sum_list = [0] * (len(arr))
num_list = [0] * m
for i in range(n):
    if n == 0:
        sum_list[0] = arr[0] % m
    else:
        sum_list[i] = (sum_list[i-1] + arr[i]) % m
    num_list[sum_list[i]] += 1

result = 0
for i in range(m):
    num = num_list[i]
    result += num * (num-1) // 2

print(result + num_list[0])