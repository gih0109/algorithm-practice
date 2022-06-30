import sys
sys.stdin = open(r"백준\집합과 맵\test.txt", "r")

S = str(input())
result = set()
for i in range(1, len(S)+1):
    for j in range(0, len(S)-i+1):
        result.add(S[j:j+i])

print(len(result))