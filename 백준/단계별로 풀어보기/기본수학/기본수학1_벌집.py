n = 7

num = 1
cnt = 1

if n > 1:
    while n > num:
        num = num + 6 * cnt
        cnt += 1

print(cnt)