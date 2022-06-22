import sys
import string
sys.stdin = open(r"누적 합\test.txt", "r")
input = sys.stdin.readline

s = str(input())
q = int(input())

# 누적합 구하기
alphabet = [i for i in string.ascii_lowercase]
check = [[0] * (len(s)) for _ in range(26)]

for alpha_idx, cnt_list in enumerate(check):
    cnt = 0
    for idx, val in enumerate(cnt_list):
        if alphabet[alpha_idx] == s[idx]:
            cnt += 1
        cnt_list[idx] = cnt

# 문제 풀기
for _ in range(q):
    a, l, r = map(str, input().split())
    if l == '0':
        print(check[ord(a)-97][int(r)])
    else:
        print(check[ord(a)-97][int(r)] - check[ord(a)-97][int(l)-1])