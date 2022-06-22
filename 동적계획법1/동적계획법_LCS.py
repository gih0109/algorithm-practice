import sys
sys.stdin =open(r"동적계획법1\test.txt", "r")

string_1 = str(input())
string_2 = str(input())

length_1 = len(string_1)
length_2 = len(string_2)

dy = [[0] * 1001 for _ in range(1001)]
string_1 = "_" + string_1
string_2 = "_" + string_2
result = 0

if length_1 == 0 or length_2 == 0:
    print(result)
else:
    for i in range(length_1 + 1):
        for j in range(length_2 + 1):
            if i == 0 or j == 0:
                dy[i][j] = 0
            elif string_1[i] == string_2[j]:
                dy[i][j] = dy[i-1][j-1] + 1
            else:
                dy[i][j] = max(dy[i-1][j], dy[i][j-1])
            if dy[i][j] > result:
                result = dy[i][j]

print(result)