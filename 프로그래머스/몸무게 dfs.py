def solution(weights):
    n = len(weights)
    A, B = [], []

    max_len, max_w = 0, 0

    def dfs(A, B, idx, weights):
        nonlocal max_len, max_w

        if sum(A) > sum(weights):
            return
        if sum(B) > sum(weights):
            return

        if sum(A) == sum(B):
            if len(A) + len(B) >= max_len:
                max_len = len(A) + len(B)
                if sum(A) > max_w:
                    print(A)
                    print(B)
                    max_w = sum(A)

        if idx == len(weights):
            return

        else:
            # weight[idx] 를 A 팀에 추가하는 경우
            A.append(weights[idx])
            dfs(A, B, idx+1, weights)
            A.pop()
            # weight[idx] 를 B 팀에 추가하는 경우
            B.append(weights[idx])
            dfs(A, B, idx+1, weights)
            B.pop()
            # 추가 X
            dfs(A, B, idx+1, weights)

    dfs(A, B, 0, weights)
    return [max_len, max_w]


if __name__ == "__main__":
    weights = [40, 50, 160, 10, 20, 130, 70, 250, 90, 100, 35, 65]
    print(solution(weights))
