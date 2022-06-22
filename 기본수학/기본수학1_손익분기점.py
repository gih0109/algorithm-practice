A = 3
B = 2
C = 1

gain = C - B

if gain <= 0:
    print(-1)
else:
    print(A // gain + 1)