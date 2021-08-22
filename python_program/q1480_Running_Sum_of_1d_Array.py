from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum_list = []
        running_sum = 0
        for i in nums:
            running_sum += i
            running_sum_list.append(running_sum)
        return running_sum_list

sol = Solution()


# input
nums = [1,2,3,4]
# output
output = sol.runningSum(nums)
# answer
answer = [1,3,6,10]
print(output, answer, answer == output)

# input
nums = [1,1,1,1,1]
# output
output = sol.runningSum(nums)
# answer
answer = [1,2,3,4,5]
print(output, answer, answer == output)

# input
nums = [3,1,2,10,1]
# output
output = sol.runningSum(nums)
# answer
answer = [3,4,6,16,17]
print(output, answer, answer == output)
