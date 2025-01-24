def longestOnes(nums: list[int], k: int) -> int:
    maxlen=0
    l=0
    for i in range(len(nums)):
        if nums[i]==0:
            k-=1
        while k<0:
            if nums[l]==0:
                k+=1
            l+=1
        maxlen=max(maxlen,i-l+1)
    return maxlen


nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
print(longestOnes(nums,k))