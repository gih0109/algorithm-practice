import sys
sys.stdin = open(r"C:\Users\송영섭\OneDrive\백준\백트래킹\input.txt", "r")

def dfs(x: int, num: int):
    global max_val, min_val

    if x == n:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    
    else:
        if op_check[0] < op_list[0]:
            op_check[0] += 1
            dfs(x + 1, num + num_list[x])
            op_check[0] -= 1
        if op_check[1] < op_list[1]:
            op_check[1] += 1
            dfs(x + 1, num - num_list[x])
            op_check[1] -= 1
        if op_check[2] < op_list[2]:
            op_check[2] += 1
            dfs(x + 1, num * num_list[x])
            op_check[2] -= 1
        if op_check[3] < op_list[3]:
            op_check[3] += 1
            if num < 0:
                dfs(x + 1, -(-num // num_list[x]))    
            else:
                dfs(x + 1, num // num_list[x])
            op_check[3] -= 1

if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))
    op_list = list(map(int, input().split()))
    # n = 2
    # num_list = [5, 6]
    # op_list = [0, 0, 3, 0]
    op_check = [0] * 4

    max_val = -1000000001
    min_val = 1000000001

    dfs(1, num_list[0])

    print(max_val)
    print(min_val)