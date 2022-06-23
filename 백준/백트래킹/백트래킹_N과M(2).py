def dfs(x, a):
    if x == m:
        for i in result:
            print(i, end=' ')
        print()

    else:
        for i in range(a+1, n+1):
            if check[i] == 0:
                check[i] = 1
                result.append(i)
                dfs(x+1, i)
                check[i] = 0
                result.pop()


if __name__ == "__main__":
    n, m = 4, 4
    check = [0] * (n + 1)
    result = []
    dfs(0, 0)