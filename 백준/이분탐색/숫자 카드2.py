import sys
sys.stdin = open(r"이분탐색\test.txt", "r")

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

# print(n, m)
# print(n_arr)
# print(m_arr)
n_arr.sort()
n_dict = dict()

for i in n_arr:
    n_dict.setdefault(i, 0)
    n_dict[i] += 1

result = []

for m_num in m_arr:
    # 이분탐색
    lp = 0
    rp = len(n_arr) - 1

    while lp <= rp:
        mid_p = (lp + rp) // 2

        if n_arr[mid_p] == m_num:
            result.append(str(n_dict[m_num]))
            break

        elif n_arr[mid_p] > m_num:
            rp = mid_p - 1

        else:
            lp = mid_p + 1
    
    else:
        result.append('0')

print(" ".join(result))
    