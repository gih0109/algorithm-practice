import sys
import heapq
sys.stdin = open(r"우선순위큐\test.txt", "r")

n = int(input())

que = []

for i in range(n):
    num = int(input())
    if num == 0:
        if len(que) > 0:
            tmp = heapq.heappop(que)
            print(-tmp)
        else:
            print(0)
    else:
        heapq.heappush(que, -num)