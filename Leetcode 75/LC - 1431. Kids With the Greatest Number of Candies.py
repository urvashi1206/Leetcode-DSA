def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    ans=[]
    maxNum=0
    for i in range(len(candies)):
        maxNum=max(candies[i],maxNum)
    
    for i in range(len(candies)):
        if candies[i]+extraCandies>=maxNum:
            ans.append(True)
        else:
            ans.append(False)
    return ans

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))