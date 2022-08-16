import sys
sys.stdin = open(r"백준\투 포인터\test.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
left_p, right_p = 0, N - 1

min_val = sys.maxsize
num_1, num_2 = 0, 0
while left_p < right_p:
    val = arr[left_p] + arr[right_p]

    if abs(val) < min_val:
        min_val = abs(val)
        num_1, num_2 = arr[left_p], arr[right_p]

    if val < 0:
        left_p += 1
    else:
        right_p -= 1

print(num_1, num_2)
