import sys
sys.stdin = open(r"정렬\test.txt", "r")

n = str(input())
arr = [i for i in n]
arr.sort(reverse=True)
print("".join(arr))
