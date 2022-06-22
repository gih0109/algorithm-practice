

def dfs(x):
    if x == m:
        for i in result:
            print(i, end=' ')
        print()
    
    else:
        for i in range(1, n + 1):
            if check[i] == 0:
                check[i] = 1
                result.append(i)
                dfs(x + 1)
                check[i] = 0
                result.pop()



if __name__ == "__main__":
    n, m = 4, 2
    check = [0] * (n + 1)
    result = []
    dfs(0)