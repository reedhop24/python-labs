import math

def binary_sort(nums, target):
    sort = sorted(nums)
    left = 0
    right = len(sort)-1
    while left <= right:
        mid = left + math.floor((right-left)/2)
        if sort[mid] == target:
            return mid
        elif sort[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_sort([6,9,10,3,4,2,69,81,5], 5))