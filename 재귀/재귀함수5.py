# n = int(input())
n = 10


def dfs(x):

    if x == 0:
        return 0
    
    if x == 1:
        return 1

    else:
        return dfs(x-1) + dfs(x-2)

print(dfs(n))