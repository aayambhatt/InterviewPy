from typing import List

def largest_container(heights: List[int]) -> int:
    # Write your code here
    n = len(heights)
    left = 0
    right = n-1
    max_water = 0

    while left < right:
        water = min(heights[left],heights[right])*(right-left)

        max_water = max(max_water, water)

        if heights[left]<heights[right]:
            left+=1
        elif heights[left]>heights[right]:
            right-=1
        else:
            left+=1
            right-=1
    
    return max_water
        