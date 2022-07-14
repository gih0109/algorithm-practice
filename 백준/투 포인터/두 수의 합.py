import sys
sys.stdin = open(r"백준\투 포인터\test.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
left_p, right_p = 0, n - 1

cnt = 0
while left_p < right_p:
    num = arr[left_p] + arr[right_p]
    if num == x:
        left_p += 1
        cnt += 1
    elif num < x:
        left_p += 1
    else:
        right_p -= 1

print(cnt)