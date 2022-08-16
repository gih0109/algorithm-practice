import sys
sys.stdin = open(r"정렬\test.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(i)