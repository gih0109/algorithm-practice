n = int(input())
for _ in range(n):
    m = int(input())
    ch = [0] * 101
    ch[1] = 1
    ch[2] = 1
    ch[3] = 1
    for i in range(3, m+1):
        ch[i] = ch[i-2] + ch[i-3]
    print(ch[m])
