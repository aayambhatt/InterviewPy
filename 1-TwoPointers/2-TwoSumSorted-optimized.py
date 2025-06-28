from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left+=1
            elif sum > target:
                right -= 1
            else:
                return [left+1, right+1]
        
        