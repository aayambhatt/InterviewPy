from typing import List

def largest_container(heights: List[int]) -> int:
    n = len(heights)
    max_water = 0

    for i in range(n):
        for j in range(i+1, n):
            water = min(heights[i],heights[j])*(j-i)
            max_water = max(max_water, water)
    
    return max_water