def selection(nums):
    n=len(nums)
    for i in range(0,n):
        min_i = i
        for j in range(i+1,n):
            if nums[j]<nums[min_i]:
                min_i = j
        nums[i],nums[min_i] = nums[min_i],nums[i]
    return nums

nums = [1,6,3,8,3,2,5,8,4,6,2]
print(selection(nums))