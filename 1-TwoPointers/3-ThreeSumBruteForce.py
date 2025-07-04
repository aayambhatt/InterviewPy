from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    triplets = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i]+nums[j]+nums[k]==0:
                    triplet = tuple(
                        sorted([nums[i], nums[j], nums[k]])
                    )
                    triplets.add(triplet)
    
    return [list(triplet) for triplet in triplets]

print(triplet_sum([0,-1,2,-3,1]))