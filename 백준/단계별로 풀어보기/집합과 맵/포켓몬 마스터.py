import sys
from collections import defaultdict
sys.stdin = open(r"집합과 맵\test.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
name_dict = defaultdict(int)
num_dict = defaultdict(str)

for num in range(1, n+1):
    poketmon = str(input().strip())
    name_dict[poketmon] = num
    num_dict[num] = poketmon

for _ in range(m):
    tmp = str(input().strip())
    if tmp.isdecimal() == True:
        print(num_dict[int(tmp)])
    else:
        print(name_dict[tmp])