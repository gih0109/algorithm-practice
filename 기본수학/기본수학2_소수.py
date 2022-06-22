N, M = 60, 100
num_list = []

for i in range(N, M+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num_list.append(i)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(num_list[0])