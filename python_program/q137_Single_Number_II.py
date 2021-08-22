from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two, three = 0, 0, 0
        for num in nums:
		
            # bit 1 show twice
            two |= (one & num) 
            
            # bit 1 show once
            one ^= num
            
            # bit 1 show three times
            three = two & one 
            
            # erase bit that show three time 1
            two = two & (~three)
            one = one & (~three)
        
        return one


sol = Solution()


# input
nums = [2,2,3,2]
# output
output = sol.singleNumber(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [0,1,0,1,0,1,99]
# output
output = sol.singleNumber(nums)
# answer
answer = 99
print(output, answer, answer == output)

