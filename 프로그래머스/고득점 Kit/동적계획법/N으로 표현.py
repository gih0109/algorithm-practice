def solution(N, number):
    if N == number:
        return 1

    dy = []

    for i in range(1, 9): # N의 갯수
        all_case = set()
        check_num = int(str(N) * i) # N, NN, NNN, ...
        all_case.add(check_num)

        for j in range(i-1): # j 개를 사용해서 만든 값들
            for op1 in dy[j]:
                for op2 in dy[-j-1]:
                    all_case.add(op1 + op2)
                    all_case.add(op1 - op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)

        if number in all_case:
            answer = i
            break

        dp.append(all_case)

    return answer

if __name__ == "__main__":
    N = 5
    number = 12
    print(solution(N, number))
