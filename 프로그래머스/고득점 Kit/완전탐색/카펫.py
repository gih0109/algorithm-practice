def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0 and (i+2) * ((yellow // i) + 2) - yellow == brown:
            return [(yellow // i) + 2, i+2]


if __name__ == "__main__":
    brown = 24
    yellow = 24
    print(solution(brown, yellow))