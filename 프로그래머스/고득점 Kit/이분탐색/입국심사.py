def solution(n, times):
    
    left, right = 1, 10 ** 20
    
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        
        for time in times:
            tmp += mid // time
            
        if tmp >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer