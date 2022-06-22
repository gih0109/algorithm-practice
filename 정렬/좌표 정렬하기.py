import sys
sys.stdin = open(r"정렬\test.txt", "r")
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key= lambda x: (x[0], x[1]))

for i in a:
    print(i[0], i[1])