def solution(money):
    n = len(money)
    dy_1 = [[0, 0] for _ in range(n)] # 정방향 더함
    dy_2 = [[0, 0] for _ in range(n)] # 역방향 더함
    dy_1[0] = [money[0], 0]
    dy_1[1] = [money[1], 1]
    dy_2[-1] = [money[-1], 0]
    dy_2[-2] = [money[-2], 1]

    max_val = max(dy_1[0][0], dy_1[1][0], dy_2[-1][0], dy_2[-2][0])

    for i in range(2, n):
        # dy_1    
        if dy_1[i-2][0] > dy_1[i-3][0]:
            tmp_1 = [dy_1[i-2][0] + money[i], dy_1[i-2][1]]
        else:
            tmp_1 = [dy_1[i-3][0] + money[i], dy_1[i-3][1]]
        # dy_2
        if dy_2[-i+1][0] > dy_2[-i+2][0]:
            tmp_2 = [dy_2[-i+1][0] + money[-i-1], dy_1[-i+1][1]]
        else:
            tmp_2 = [dy_2[-i+2][0] + money[-i-1], dy_1[-i+2][1]]

        if i == n - 1:
            if tmp_1[1] == 0:
                continue
            else:
                dy_1[i] = tmp_1

            if tmp_2[1] == 0:
                continue
            else:
                dy_2[-i-1] = tmp_2

        else:
            dy_1[i] = tmp_1
            dy_2[-i-1] = tmp_2

        # 최대값 갱신
        if dy_1[i][0] > max_val:
            max_val = dy_1[i][0]

        if dy_2[-i-1][0] > max_val:
            max_val = dy_2[-i-1][0]

    return max_val


if __name__ == "__main__":
    money = [15, 2, 8, 20, 6, 13, 1]
    print(solution(money))