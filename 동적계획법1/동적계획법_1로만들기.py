n = 10

if n == 1:
    print(0)

else:
    dy = []
    dy.append([n])
    cnt = 0
    break_check = 0
    while break_check != 1:
        dy_temp = []
        for i in dy[-1]:
            if i % 3 == 0:
                temp = i // 3
                if temp == 1:
                    break_check = 1
                    break
                dy_temp.append(temp)
            if i % 2 == 0:
                temp = i // 2
                if temp == 1:
                    break_check = 1
                    break
                dy_temp.append(temp)
            dy_temp.append(i-1)
        dy.append(dy_temp)
        cnt += 1

    print(cnt)