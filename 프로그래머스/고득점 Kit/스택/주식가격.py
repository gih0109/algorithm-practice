def solution(prices):
    answer = [0] * len(prices)
    stack = []

    # 가장 마지막 주식가격 변화는 항상 0
    for idx, val in enumerate(prices[:-1]):
        # stack 이 있고 val 이 stack[-1] 보다 같거나 클때까지 stack pop
        while stack and stack[-1][1] > val:
            tmp = stack.pop()
            answer[tmp[0]] = tmp[2]
        # stack 에 추가
        stack.append([idx, val, 0])
        # 시간 += 1
        for i in range(len(stack)):
            stack[i][2] += 1
            
    # stack 잔여해있는 것 answer 로 시간 값 전달
    for idx, num, time in stack:
        answer[idx] = time
    
    return answer