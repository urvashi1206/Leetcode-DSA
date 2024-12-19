def pivotIndex(nums: list[int]) -> int:
    sum=0
    left=0
    for i in range(len(nums)):
        sum+=nums[i]
    
    for i in range(len(nums)):
        sum-=nums[i]
        if(sum==left):
            return i
        left+=nums[i]
    
    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))