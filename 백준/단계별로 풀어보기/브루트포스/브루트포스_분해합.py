n = 216

for i in range(1, n+1):
    tmp = i + sum(int(j) for j in str(i))
    if tmp == n:
        print(i)
        break
else:
    print(0)