import sys
sys.stdin = open(r"백준\분할 정복\test.txt", "r")
input = sys.stdin.readline


# 좌우로 탐색하여 가장 큰 사각형 넓이를 구하는 함수
def find_max(nums, left, right, mid):
    mid_r, mid_l = mid + 1, mid
    tmp_h = min(nums[mid_l], nums[mid_r])
    width = 2
    result = tmp_h * width

    while True:
        if (nums[mid_l] == 0 or mid_l == left) and (nums[mid_r] == 0 or mid_r == right):
            break

        if mid_l == left or nums[mid_l] == 0:
            mid_r += 1

        elif mid_r == right or nums[mid_r] == 0:
            mid_l -= 1

        else:
            if nums[mid_r + 1] > nums[mid_l - 1]:
                mid_r += 1
            else:
                mid_l -= 1
        width += 1

        tmp_h = min(tmp_h, nums[mid_l], nums[mid_r])
        area = tmp_h * width
        if area > result:
            result = area

    return result


# 분할정복
def divide(nums, left, right):
    if left == right:
        return nums[left]
    else:
        mid = (left + right) // 2
        return max(divide(nums, left, mid), divide(nums, mid+1, right), find_max(nums, left, right, mid))


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    # print(nums)
    print(divide(nums, 1, nums[0]))

