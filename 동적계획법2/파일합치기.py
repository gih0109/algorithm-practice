import sys
sys.stdin = open(r"동적계획법2\test.txt", "r")

t = int(input())

for _ in range(t):
    k = int(input())
    arr = [0] + list(map(int, input().split()))
    # print(arr)

    # 누적합
    sum_arr = [0] * (k+1)
    sum_arr[0] = arr[0]
    for i in range(1, k+1):
        sum_arr[i] = sum_arr[i-1] + arr[i]
    # print(sum_arr)

    dy = [[0] * (k+1) for _ in range(k+1)]

    # 파일의 길이
    for i in range(2, k+1):
        # 시작점
        for j in range(1, k+2-i):
            dy[j][j+i-1] = min([dy[j][j+l] + dy[j+l+1][j+i-1] for l in range(i-1)]) + (sum_arr[j+i-1] - sum_arr[j-1])

    print(dy[1][k])

