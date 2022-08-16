def solution(n, s):
    if s // n < 1:
        return [-1]
    
    num_list = [s // n] * n
    rest = s % n
    
    for i in range(rest):
        num_list[i % rest] += 1
    
    num_list.sort()
    return num_list