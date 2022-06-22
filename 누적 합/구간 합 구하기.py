import sys
sys.stdin = open(r"누적 합\test.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dy = [0] * (len(arr) + 1)
dy[1] = arr[0]

for i in range(1, len(arr)):
    dy[i+1] = arr[i] + dy[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(dy[j] - dy[i-1])