import sys
sys.stdin = open(r"누적 합\test.txt", "r")

n, k = map(int, input().split())
temp = list(map(int, input().split()))

print(n, k)
print(temp)

sum_val = sum(temp[0:k])
max_val = sum_val
for i in range(len(temp)-k):
    sum_val = sum_val - temp[i] + temp[i+k]
    if sum_val > max_val:
        max_val = sum_val

print(max_val)