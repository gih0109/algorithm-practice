from collections import defaultdict

def solution(answers):
    man_1 = [1, 2, 3, 4, 5]
    man_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0, 0]

    for idx, val in enumerate(answers):
        if man_1[idx%5] == val:
            cnt[1] += 1
        if man_2[idx%8] == val:
            cnt[2] += 1
        if man_3[idx%10] == val:
            cnt[3] += 1
    
    answer = []
    for idx, val in enumerate(cnt):
        if val == max(cnt):
            answer.append(idx)
    
    return answer

if __name__ == "__main__":
    answers = [1, 3, 2, 4, 2]
    print(solution(answers))