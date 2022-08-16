def solution(n):
    str_set = set(["()"])
    
    def dfs(x):
        nonlocal str_set
        
        if x == n:
            return

        tmp_set = set()
        
        for i in list(str_set):
            tmp_set.add("(" + i + ")")
            tmp_set.add("()" + i)
            tmp_set.add(i + "()")
        
        str_set = tmp_set

        dfs(x+1)
    
    dfs(1)
    print(str_set)
    return len(str_set)

if __name__ == "__main__":
    n = 4
    print(solution(n))