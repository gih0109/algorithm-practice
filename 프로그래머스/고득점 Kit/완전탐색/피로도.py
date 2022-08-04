def solution(k, dungeons):
    answer = 0
    check = [0] * len(dungeons)
    
    def dfs(k, cnt, dungeons, check):
        nonlocal answer

        if cnt > answer:
            answer = cnt

        for idx, val in enumerate(dungeons):
            if k >= val[0] and check[idx] == 0:
                check[idx] = 1
                dfs(k-val[1], cnt+1, dungeons, check)
                check[idx] = 0

    dfs(k, 0, dungeons, check)
    
    return answer

if __name__ == "__main__":
    dungeons = [[80,20],[50,40],[30,10]]
    k = 80
    print(solution(k, dungeons))