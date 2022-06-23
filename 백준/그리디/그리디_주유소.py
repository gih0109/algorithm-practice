import sys
sys.stdin = open(r"그리디\test.txt", "r")

n = int(input())
distance = list(map(int, input().split()))
city = list(map(int, input().split()))

result = 0
pointer = 0
sum_distance = distance[0]
min_price = city[0]
for i in range(1, len(city)):
    if i == len(city) - 1:
        result += city[pointer] * (sum_distance)
        break
    if city[i] < min_price:
        result += city[pointer] * (sum_distance)
        sum_distance = distance[i]
        min_price = city[i]
        pointer = i
    else:
        sum_distance += distance[i]

print(result)