def solution(n, money):
    dy = [0] * (n + 1)
    dy[0] = 1 # 거스름돈 - 동전금액 = 0 일때 동전갯수가 1이 되므로 점화식에서 dy[j-i] == 0 이 될때 +1 이 되도록 참조용
    for i in money:
        for j in range(i, n+1): 
            # 점화식, 거스름돈 경우 수 = 현재 동전 경우의 수 + 현재 동전금액을 제외한 잔액의 경우의 수
            dy[j] = (dy[j] + dy[j-i]) % 1000000007
            
    return dy[-1]

if __name__ == "__main__":
    n = 5
    money = [1, 2, 5]
    print(solution(n, money))