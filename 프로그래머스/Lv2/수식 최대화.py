from itertools import permutations

def cal(a, b, operation):
    result = 0
    if operation == "+":
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == "*":
        result = a * b
    return str(result)

def solution(expression):
    opr = ["+", "-", "*"]
    exp_list = []
    tmp = ''
    for i in expression:
        if i.isdecimal() == True:
            tmp += i
        else:
            exp_list.append(tmp)
            exp_list.append(i)
            tmp = ''
    else:
        exp_list.append(tmp)
    
    tmp_exp_list = exp_list
    opr_list = list(permutations(opr))
    # print(opr_list)
    
    max_val = 0
    for i in opr_list:

        for j in i:
            stack = []
            for k in range(len(tmp_exp_list)):
                if len(stack) >= 2 and stack[-1] == j:
                    tmp = cal(int(stack[-2]), int(tmp_exp_list[k]), j)
                    for _ in range(2):
                        stack.pop()
                    stack.append(tmp)
                else:
                    stack.append(tmp_exp_list[k])

            if len(stack) == 1:
                if abs(int(stack[0])) > max_val:
                    max_val = abs(int(stack[0]))
            tmp_exp_list = stack

        tmp_exp_list = exp_list

    return max_val


if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))