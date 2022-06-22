import sys
import heapq as hq
sys.stdin = open(r"우선순위큐\test.txt", "r")
input = sys.stdin.readline

a = []
n = int(input())

for i in range(n):
    tmp = int(input())
    if tmp == 0:
        if len(a) > 0:
            val = hq.heappop(a)
            print(val[1])
        else:
            print(0)
    else:
        hq.heappush(a, (abs(tmp), tmp))