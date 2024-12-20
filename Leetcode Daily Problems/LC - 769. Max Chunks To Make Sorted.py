def maxChunksToSorted(arr: list[int]) -> int:
    max_Sum=0
    chunks=0
    for i in range(len(arr)):
        max_Sum=max(arr[i],max_Sum)
        if max_Sum==i:
            chunks+=1
    return chunks

arr = [4,3,2,1,0]
print(maxChunksToSorted(arr))