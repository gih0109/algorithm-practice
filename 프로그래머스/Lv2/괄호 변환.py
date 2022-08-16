# 올바른 괄호 문자열 확인
def check(a: str):
    stack = []
    for i in a:
        if stack and stack[-1] == "(" and i == ")":
            stack.pop()
        else:
            stack.append(i)
    if len(stack):
        return False
    else:
        return True

# 괄호 변환
def change_string(p):
    if p == "":
        return p

    u, v = "", ""
    cnt = 0
    for idx, string in enumerate(p):
        if idx > 0 and cnt == 0:
            v = p[idx:]
            break
        if string == "(":
            cnt -= 1
            u += string
        else:
            cnt += 1
            u += string
    
    if check(u) == True:
        return u + change_string(v)
    else:
        tmp_u = ""
        for i in u[1:-1]:
            if i == "(":
                tmp_u += ")"
            else:
                tmp_u += "("
        return "(" + change_string(v) + ")" + tmp_u
        
def solution(p):
    
    answer = change_string(p)
    return answer

if __name__ == "__main__":
    p = ")("
    print(solution(p))