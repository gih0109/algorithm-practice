import sys
sys.stdin = open(r"분할 정복\test.txt", "r")
input = sys.stdin.readline

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


# 행렬 곱셈 
def mul(arr1: list, arr2: list, n: int) -> list:
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += arr1[i][k] * arr2[k][j]
            result[i][j] %= 1000
    return result


# 행렬 분할 정복 
def power(arr: list, b: int) -> list:
    if b == 1:
        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] %= 1000
        return arr

    temp = power(arr, b//2)
    if b % 2 == 0:
        return mul(temp, temp, n)
    else:
        return mul(mul(temp, temp, n), arr, n)


answer = power(arr, b)
for row in answer:
    for num in row:
        print(num, end=' ')
    print()