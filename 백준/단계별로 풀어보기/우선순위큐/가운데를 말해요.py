import sys
import heapq as hq
sys.stdin = open(r"우선순위큐\test.txt", "r")

n = int(input())
max_heap = [] # 최대힙
min_heap = [] # 최소힙

for _ in range(n):
    num = int(input())

    if len(max_heap) == 0:
        hq.heappush(max_heap, -num)
        print(-max_heap[0])
    
    else:
        if len(max_heap) == len(min_heap):
            if num < -max_heap[0]:
                hq.heappush(max_heap, -num)
            else:
                hq.heappush(min_heap, num)

            if len(max_heap) < len(min_heap):
                hq.heappush(max_heap, -hq.heappop(min_heap))
            print(-max_heap[0])

        else:
            if num < -max_heap[0]:
                hq.heappush(min_heap, -hq.heappop(max_heap))
                hq.heappush(max_heap, -num)
            else:
                hq.heappush(min_heap, num)
            print(-max_heap[0])
    