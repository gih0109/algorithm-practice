import sys
sys.stdin = open(r"정렬\test.txt", "r")
input = sys.stdin.readline

n = int(input())
words = set(str(input().strip()) for _ in range(n))
words = list(words)
words.sort(key= lambda x: (len(x), x))

for word in words:
    print(word)