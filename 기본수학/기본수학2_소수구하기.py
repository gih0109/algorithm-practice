M, N = 3, 16

num_check = [0] * (N + 1)

for i in range(2, N + 1):
    if num_check[i] == 0:
        if i >= M:
            print(i)
        for j in range(i, N + 1, i):
            num_check[j] = 1
