import sys
sys.stdin = open(r"이분탐색\test.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
lis = [0] * n
lis[0] = arr[0]
pointer = 0

for idx in range(1, n):
    if arr[idx] > lis[pointer]:
        lis[pointer+1] = arr[idx]
        pointer += 1
    elif arr[idx] < lis[pointer]:
        lp = 0
        rp = pointer
        while lp <= rp:
            midp = (lp + rp) // 2
            if lis[midp] >= arr[idx]:
                rp = midp - 1
            else:
                lp = midp + 1
        lis[lp] = arr[idx]

# print(lis)
print(pointer+1)

