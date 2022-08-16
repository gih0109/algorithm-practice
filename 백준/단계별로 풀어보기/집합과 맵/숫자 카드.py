import sys
sys.stdin = open(r"집합과 맵\test.txt", "r")
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for i in B :
    if i in A :
        print(1, end=' ')

    else :
        print(0, end=' ')