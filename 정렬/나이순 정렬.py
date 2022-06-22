import sys
sys.stdin = open(r"정렬\test.txt", "r")
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    num, name = map(str, input().split())
    num = int(num)
    a.append([num, name, i])

a.sort(key= lambda x: (x[0], x[2]))
print(a)

for i in a:
    print(i[0], i[1])