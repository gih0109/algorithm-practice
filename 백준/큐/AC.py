import sys
from collections import deque
sys.stdin = open(r"큐\test.txt", "r")
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    command = str(input())
    n = int(input())
    n_list = list(input()[1:-2].split(','))
    if n_list == ['']: 
        n_list = []
    
    r = 0
    lp = 0
    rp = 0
    for i in command:
        if lp > n - rp:
            print('error')
            break
        if i == "R":
            if r == 0:
                r = 1
            else:
                r = 0
        elif i == "D":
            if r == 0:
                lp += 1
            else:
                rp += 1
    else:
        if r == 1:
            n_list.reverse()
            lp, rp = rp, lp
        n_list = n_list[lp:n - rp]
        print("[" + ",".join(n_list) + "]")
