# 수정필요

def solution(money):
    n = len(money)
    dy = [[0, 0] for _ in range(n)]
    dy[0] = [money[0], 0]
    dy[1] = [money[1], 1]
    dy[2] = [money[0] + money[2], 0]

    max_val = max(money[0], money[1], money[2])
    if n > 3:
        max_val = max(dy[0][0], dy[1][0], dy[2][0])

        for i in range(3, n):
            if i == n - 1:
                tmp = []
                if dy[i-2][1]:
                    tmp.append(dy[i-2][0] + money[i])
                if dy[i-3][1]:
                    tmp.append(dy[i-3][0] + money[i])
                if tmp:
                    dy[i] = [max(tmp), 1]

            else:    
                if dy[i-2][0] > dy[i-3][0]:
                    dy[i] = [dy[i-2][0] + money[i], dy[i-2][1]]
                else:
                    dy[i] = [dy[i-3][0] + money[i], dy[i-3][1]]

            if dy[i][0] > max_val:
                max_val = dy[i][0]

    return max_val


if __name__ == "__main__":
    money = [2, 8, 20, 6, 13, 1, 15]
    print(solution(money))