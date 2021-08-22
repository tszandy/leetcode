from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = 1
        max_product = float("-inf")
        for num in nums:
            product *= num
            max_product = max(product,max_product)
            if product ==0:
                product = 1
            
        product = 1
        for num in nums[::-1]:
            product *= num
            max_product = max(product,max_product)
            if product ==0:
                product = 1
            
        return max_product

sol = Solution()


# input
nums = [2,3,-2,4]
# output
output = sol.maxProduct(nums)
# answer
answer = 6
print(output, answer, answer == output)

# input
nums = [-2,0,-1]
# output
output = sol.maxProduct(nums)
# answer
answer = 0
print(output, answer, answer == output)
