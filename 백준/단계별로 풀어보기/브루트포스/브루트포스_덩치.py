import sys
sys.stdin = open(r"브루트포스\test.txt", "r")

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
# print(n_list)
result = []

