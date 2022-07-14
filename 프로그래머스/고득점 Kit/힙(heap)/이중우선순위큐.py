import heapq as hq

def solution(operations):
    n = len(operations)
    heap = []

    for command in operations:        
        if command == "D 1":
            if len(heap):
                for idx, val in enumerate(heap):
                    heap[idx] = -val
                hq.heapify(heap)
                hq.heappop(heap)
                for idx, val in enumerate(heap):
                    heap[idx] = -val
                hq.heapify(heap)
        
        elif command == "D -1":
            if len(heap):
                hq.heappop(heap)

        else:
            _, num = command.split()
            hq.heappush(heap, int(num))

    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]


if __name__ == "__main__":
    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    # operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))