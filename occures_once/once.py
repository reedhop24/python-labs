def occures_once(nums):
    sort = sorted(nums)
    for i, j in enumerate(sort):
        if j != sort[i-1] and j != sort[i+1]:
            return j

print(occures_once([1,2,3,4,5,6,1,3,4,5,6,1,3,4,5,6]))