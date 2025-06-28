from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    # The 'left' pointer is used to position non-zero elements.
    left = 0

    for right in range(len(nums)):
        if nums[right]!=0:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1

    

