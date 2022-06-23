def dfs(x):
    if x == m:
        for i in result:
            print(i, end=' ')
        print()
    
    else:
        for i in range(1, n + 1):
                result.append(i)
                dfs(x + 1)
                result.pop()

if __name__ == "__main__":
    n, m = 3, 3
    check = [0] * (n + 1)
    result = []
    dfs(0)