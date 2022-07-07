def solution(numbers, hand):
    Keypad = {
        1: 1, 2: 1, 3: 1,
        4: 2, 5: 2, 6: 2,
        7: 3, 8: 3, 9: 3,
        0: 4, "*": 4, "#": 4} # 거리
    L = (1, 4, 7, "*") # 왼손
    R = (3, 6, 9, "#") # 오른손
    M = (2, 5, 8, 0) # 가운데
    
    answer = ''
    last_l, last_r = "*", "#" # 왼쪽 오른쪽 손가락 초기 위치
    last_p = -1 # 마지막으로 누른 값

    for num in numbers:
        if num in L:
            last_l = num
            last_p = Keypad[num]
            answer += "L"

        elif num in R:
            last_r = num
            last_p = Keypad[num]
            answer += "R"

        else:
            if last_l in M and last_r in M:
                if abs(Keypad[num] - Keypad[last_l]) < abs(Keypad[num] - Keypad[last_r]):
                    last_l = num
                    answer += "L"
                elif abs(Keypad[num] - Keypad[last_l]) > abs(Keypad[num] - Keypad[last_r]):
                    last_r = num
                    answer += "R"
                else:
                    if hand == "right":
                        last_r = num
                        answer += "R"
                    else:
                        last_l = num
                        answer += "L"
            elif last_l in M:
                if abs(Keypad[num] - Keypad[last_l]) < abs(Keypad[num] - Keypad[last_r]) + 1:
                    last_l = num
                    answer += "L"
                elif abs(Keypad[num] - Keypad[last_l]) > abs(Keypad[num] - Keypad[last_r]) + 1:
                    last_r = num
                    answer += "R"
                else:
                    if hand == "right":
                        last_r = num
                        answer += "R"
                    else:
                        last_l = num
                        answer += "L"
            elif last_r in M:
                if abs(Keypad[num] - Keypad[last_l]) + 1 < abs(Keypad[num] - Keypad[last_r]):
                    last_l = num
                    answer += "L"
                elif abs(Keypad[num] - Keypad[last_l]) + 1 > abs(Keypad[num] - Keypad[last_r]):
                    last_r = num
                    answer += "R"
                else:
                    if hand == "right":
                        last_r = num
                        answer += "R"
                    else:
                        last_l = num
                        answer += "L"
            else:
                if abs(Keypad[num] - Keypad[last_l]) < abs(Keypad[num] - Keypad[last_r]):
                    last_l = num
                    answer += "L"
                elif abs(Keypad[num] - Keypad[last_l]) > abs(Keypad[num] - Keypad[last_r]):
                    last_r = num
                    answer += "R"
                else:
                    if hand == "right":
                        last_r = num
                        answer += "R"
                    else:
                        last_l = num
                        answer += "L"
            
    return answer

if __name__ == "__main__":
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    print(solution(numbers, hand))