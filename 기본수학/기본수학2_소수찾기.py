n = 4
n_list = [1, 3, 6, 7]

cnt = 0
for i in n_list:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            cnt += 1

print(cnt)