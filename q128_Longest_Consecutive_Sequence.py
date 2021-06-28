from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_consecutive_length = 0
        nums_set = set(nums)
        
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_consecutive_length = 1
                
                while current_num + 1 in nums_set:
                    current_num +=1
                    current_consecutive_length +=1
                    
                if current_consecutive_length > longest_consecutive_length:
                    longest_consecutive_length = current_consecutive_length
        return longest_consecutive_length

sol = Solution()


# input
nums = [100,4,200,1,3,2]
# output
output = sol.longestConsecutive(nums)
# answer
answer = 4
print(output, answer, answer == output)

# input
nums = [0,3,7,2,5,8,4,6,0,1]
# output
output = sol.longestConsecutive(nums)
# answer
answer = 9
print(output, answer, answer == output)
