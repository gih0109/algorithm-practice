n = 4

stair_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

cnt = 2
while cnt < n:
    tmp_list = []
    for _ in range(len(stair_num)):
        tmp = stair_num.pop()
        tmp1, tmp2 = int(tmp[-1]) + 1, int(tmp[-1]) - 1
        if 0 <= tmp1 < 10:
            tmp_list.append(str(tmp) + str(tmp1))
        if 0 <= tmp2 < 10:
            tmp_list.append(str(tmp) + str(tmp2))
    else:
        stair_num = tmp_list
        stair_num.sort()
        print(cnt, len(stair_num))
        print(stair_num)
    cnt += 1