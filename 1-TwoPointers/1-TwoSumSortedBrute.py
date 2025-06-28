from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
            
    return []

print(pair_sum_sorted([-5,-2, 3,4,6], 7))