def dfs(x, a):
    if x == m:
        for i in result:
            print(i, end=' ')
        print()

    else:
        for i in range(a, n+1):
            result.append(i)
            dfs(x+1, i)
            result.pop()

if __name__ == "__main__":
    n, m = 4, 2
    result = []
    dfs(0, 1)