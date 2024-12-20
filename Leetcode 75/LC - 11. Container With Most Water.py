def maxArea(height: list[int]) -> int:
    i=0
    j=len(height)-1
    maxArea=min(height[i],height[j])*(j-i)

    while(i<j):
        if (height[i]<height[j]):
            i+=1
        else:
            j-=1
        area=min(height[i],height[j])*(j-i)
        maxArea=max(maxArea,area)
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))