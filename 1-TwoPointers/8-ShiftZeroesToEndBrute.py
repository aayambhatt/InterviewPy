from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    temp = [0]*len(nums)
    # Pointer i will tell us where to place the next non-zero value in temp.
    i = 0
    # add all non zero elements to left of temp
    for num in nums:
        if num!=0:
            temp[i]=num
            i+=1
    # set nums to temp
    for j in range(len(nums)):
        nums[j]=temp[j]
    

