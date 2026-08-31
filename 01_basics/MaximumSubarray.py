def maxsubArray(nums):
    current=nums[0]
    maxsum=nums[0]

    for num in nums[1:]:
        current=max(num,current+num)
        maxsum=max(maxsum,current)
    return maxsum


print(maxsubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6