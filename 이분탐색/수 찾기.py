import sys
sys.stdin = open(r"이분탐색\test.txt", "r")

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list  = list(map(int, input().split()))

for num in m_list:
    lp = 0
    rp = len(n_list)

    while lp <= rp:
        mid_p = (lp + rp) // 2
        if n_list[mid_p] == num:
            print(1)
            break
        elif n_list[mid_p] > num:
            rp = mid_p - 1
        else:
            lp = mid_p + 1
    else:
        print(0)