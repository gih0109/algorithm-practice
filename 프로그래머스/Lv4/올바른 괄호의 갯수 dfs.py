from collections import deque

def solution(n):
    string = deque(["("])
    result = 0
    
    def dfs(x, string):
        nonlocal result
        
        if x == n * 2:
            stack = deque()
            for idx in range(n * 2):
                tmp = string[idx]
                if stack and stack[-1] == "(" and tmp == ")":
                    stack.pop()
                else:
                    stack.append(tmp)

            if len(stack) == 0:
                print(*string)
                result += 1
            return

        string.append("(")
        dfs(x+1, string)
        string.pop()
        string.append(")")
        dfs(x+1, string)
        string.pop()
    
    dfs(1, string)
    return result


if __name__ == "__main__":
    n = 4
    print(solution(n))