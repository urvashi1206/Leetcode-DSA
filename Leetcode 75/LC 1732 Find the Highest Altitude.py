def largestAltitude(gain: list[int]) -> int:
        maxSum=0
        sum=0
        for i in range(len(gain)):
            sum+=gain[i]
            maxSum=max(maxSum,sum)
        
        return maxSum
    
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))