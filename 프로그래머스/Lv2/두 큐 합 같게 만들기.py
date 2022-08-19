from collections import deque

def solution(queue1, queue2):
    deque1, deque2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(deque1), sum(deque2)
    half_sum = (sum1 + sum2) // 2
    answer = -1
    if (sum1 + sum2) % 2:
        return answer
    
    cnt = 0
    while deque1 and deque2:
        if sum1 > half_sum:
            tmp = deque1.popleft()
            sum1 = sum1 - tmp
        elif sum1 < half_sum:
            tmp = deque2.popleft()
            deque1.append(tmp)
            sum1 = sum1 + tmp
        else:
            answer = cnt
            break
            
        cnt += 1
        
    return answer


if __name__ == "__main__":
    queue1 = [1, 1, 1, 8, 10, 9]
    queue2 = [1, 1, 1, 1, 1, 1]
    print(solution(queue1, queue2))