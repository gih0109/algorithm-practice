import sys
input = sys.stdin.readline


def merge_sort(lt, rt):
    if lt < rt:
        mid_t = (lt + rt) // 2

        merge_sort(lt, mid_t)
        merge_sort(mid_t + 1, rt)
        p1 = lt
        p2 = mid_t + 1
        temp = []

        while p1 <= mid_t and p2 <= rt:
            if n_list[p1] < n_list[p2]:
                temp.append(n_list[p1])
                p1 += 1
            else:
                temp.append(n_list[p2])
                p2 += 1
        if p1 <= mid_t:
            temp = temp + n_list[p1 : mid_t+1]
        if p2 <= rt:
            temp = temp + n_list[p2 : rt + 1]
        
        for i in range(len(temp)):
            n_list[lt + i] = temp[i]


if __name__ == "__main__":
    # n = 5
    n_list = [5, 4, 3, 12, 2, 1, 6, 7, 10, 9, 8, 11]
    lt = 0
    rt = len(n_list) - 1
    merge_sort(lt, rt)
    for i in n_list:
        print(i)