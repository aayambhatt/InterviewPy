from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        
        for i in range(len(nums)):
            # optimization: will never sum to 0 
            if nums[i]>0:
                break
            if i > 0 and nums[i]==nums[i-1]:
                continue 
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total == 0:
                    triplets.append([nums[i],nums[left],nums[right]])

                    # skip duplicates left
                    while left < right and nums[left]==nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left+=1
                    right-=1
                    
                
                elif total < 0:
                    left+=1
                else:
                    right -= 1

        return triplets
                


                    

        