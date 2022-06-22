n, m = 10, 500
card_list = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
# n, m = 5, 21
# card_list = [5, 6, 7, 8, 9]

result = 0
num = 0
for i in range(n):
    num += card_list[i]
    for j in range(i+1, n):
        num += card_list[j]
        for k in range(j+1, n):
            num += card_list[k]
            if num <= m and num > result:
                result = num
            num -= card_list[k]
        num -= card_list[j]
    num -= card_list[i]
print(result)