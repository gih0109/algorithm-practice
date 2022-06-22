import sys
from collections import deque

n, k = 7, 3

result = []
a = deque([i for i in range(1, n + 1)])

cnt = 1
while a:
    if cnt == k:
        result.append(a.popleft())
        cnt = 1
    else:
        a.append(a.popleft())
        cnt += 1

answer = "<"
for i in range(n - 1):
    answer += str(result[i])
    answer += ", "
else:
    answer += str(result[-1]) + ">"

print(answer)