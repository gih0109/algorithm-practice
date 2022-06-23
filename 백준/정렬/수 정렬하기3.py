import sys
sys.stdin = open(r"정렬\test.txt", "r")
input = sys.stdin.readline

n = int(input())
count = [0] * 10001

for _ in range(n):
    num = int(input())
    count[num] += 1

for idx, val in enumerate(count):
    if count[idx] > 0:
        for j in range(val):
            print(idx)