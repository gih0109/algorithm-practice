def solution(new_id):
    allow = [".", "-", "_"]
    tmp = ""
    # 1, 2, 3
    for string in new_id:
        if string.isalpha():
            tmp += string.lower()
        elif string.isdigit():
            tmp += string
        elif string in allow:
            if tmp and tmp[-1] == "." and string == ".":
                continue
            tmp += string
    # 4
    if tmp and tmp[0] == ".": 
        tmp = tmp[1: ]
    if tmp and tmp[-1] == ".": 
        tmp = tmp[:-1]
    # 5
    if tmp == "":
        tmp = "a"
    # 6
    if len(tmp) > 15:
        tmp = tmp[:15]
        if tmp[-1] == ".": 
            tmp = tmp[:-1]
    # 7
    if len(tmp) <= 2:
        while len(tmp) < 3:
            tmp += tmp[-1]
        
    return tmp

if __name__ == "__main__":
    new_id = "abcdefghijklmn.p"
    print(solution(new_id))