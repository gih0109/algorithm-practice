X = 8

num1 = 0
cnt = 1
while X > num1:
    num1 += cnt
    cnt += 1

cnt -= 1
num2 = X - (num1 - cnt)

if cnt % 2 == 0:
    print(f"{num2}/{cnt - num2 + 1}")
else:
    print(f"{cnt - num2 + 1}/{num2}")
        