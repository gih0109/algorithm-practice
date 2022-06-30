import sys
sys.stdin = open(r"백준\정수론 및 조합론\test.txt", "r")

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[0] * nums[-1])