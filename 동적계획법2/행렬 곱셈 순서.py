import sys
sys.stdin = open(r"동적계획법2\test.txt", "r")
# input = sys.stdin.readline

n = int(input())
arr  = [list(map(int, input())) for _ in range(n)]
# sum_arr = [0] * n

dy = [[0] * (n+1) for _ in range(n+1)]

