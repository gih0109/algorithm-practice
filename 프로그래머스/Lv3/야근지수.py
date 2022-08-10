def solution(n, works):
    works.sort() # 위로 갈수록 큰 stack을 만든다

    while n:    
        tmp = works.pop()
        cnt = 1
        n = n - 1
        # stack[-1] 이 tmp 와 같을 경우 n번 이하까지 계속 pop 
        while works and tmp == works[-1] and n: 
            works.pop()
            cnt += 1
            n -= 1
        
        # 스택 뒤에 pop 한 숫자 -1 만큼 리스트 더해서 스택을 다시 만든다
        works = works + ([tmp-1] * cnt)

    answer = 0
    for i in works:
        if i > 0:
            answer += i ** 2
    return answer

if __name__ == "__main__":
    works = [1,1]
    n = 3
    print(solution(n, works))