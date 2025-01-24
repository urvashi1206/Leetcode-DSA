def maxOperations(nums: list[int], k: int) -> int:
    nums.sort()
    print(nums)
    i=0
    j=len(nums)-1
    count=0
    while i<j:
        sumNum=nums[i]+nums[j]
        if sumNum==k:
            count+=1
            i+=1
            j-=1
        elif sumNum<k:
            i+=1
        else:
            j-=1
    return count


nums = [1,2,3,4]
k = 5
print(maxOperations(nums,k))