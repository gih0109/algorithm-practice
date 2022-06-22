import sys
sys.stdin = open(r"집합과 맵\test.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
n_set = set([str(input().strip()) for _ in range(n)])
m_list = [str(input().strip()) for _ in range(m)]


cnt = 0
for i in m_list:
    if i in n_set:
        cnt += 1

print(cnt)