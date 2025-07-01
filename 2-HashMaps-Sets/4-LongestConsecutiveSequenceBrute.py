from typing import List

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    # Write your code here
    if not nums:
        return 0
    
    longest_chain = 0

    for num in nums:
        current_num = num
        current_chain = 1

        while (current_num+1) in nums:
            current_num+=1
            current_chain+=1
        
        longest_chain = max(longest_chain, current_chain)
    
    return longest_chain