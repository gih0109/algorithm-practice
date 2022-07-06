def solution(word):
    cnt_list = [781, 156, 31, 6, 1]
    str_dict = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}

    num = 0
    for idx, val in enumerate(word):
        num += str_dict[val] * cnt_list[idx] + 1
        
    return num 

if __name__ == "__main__":
    word = "EIO"
    print(solution(word))