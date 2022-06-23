import sys
sys.stdin = open(r"집합과 맵\test.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = [str(input().strip()) for _ in range(n)]
m_set = set([str(input().strip()) for _ in range(m)])

result = []
for name in n_list:
    if name in m_set:
        result.append(name)

result.sort()
print(len(result))
for i in result:
    print(i)