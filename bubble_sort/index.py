def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(0, (n-i)-1):
            if nums[j] > nums[j+1]:
                pointer = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = pointer

    return nums

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))