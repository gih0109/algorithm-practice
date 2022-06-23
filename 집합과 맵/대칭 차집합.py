import sys
sys.stdin = open(r"집합과 맵\test.txt", "r")
input = sys.stdin.readline

len_A, len_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result_1 = A - B
result_2 = B - A

print(len(result_1) + len(result_2))