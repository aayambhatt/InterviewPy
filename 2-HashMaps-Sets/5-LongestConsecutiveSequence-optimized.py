from typing import List

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    longest_chain = 0

    for num in num_set:
        # start counting the chain when we find the beginning of chain
        if num - 1 not in num_set:
            current_num = num
            current_chain = 1
            # expand the chain
            while(current_num+1) in num_set:
                current_num+=1
                current_chain+=1
            
            longest_chain = max(longest_chain, current_chain)
    
    return longest_chain

