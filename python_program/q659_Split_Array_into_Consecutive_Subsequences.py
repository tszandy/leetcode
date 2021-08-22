from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np

from collections import Counter as C

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        nums_counter = Counter(nums)
        
        track_list_of_one_num = track_list_of_two_num_except_one_num = track_extendable_list_count = 0
        for num in range(nums[0],nums[-1]+1):
            count_num = nums_counter[num]
            count_num -= track_list_of_one_num + track_list_of_two_num_except_one_num
            if count_num<0:
                return False
            
            difference_track_extendable_list_count = min(count_num,track_extendable_list_count)
            
            track_list_of_one_num, track_list_of_two_num_except_one_num,track_extendable_list_count = \
            count_num - difference_track_extendable_list_count,track_list_of_one_num, track_list_of_two_num_except_one_num+difference_track_extendable_list_count
        
        return track_list_of_one_num == track_list_of_two_num_except_one_num == 0


sol = Solution()


# input
nums = [3,4,5,6,7,8]
# output
output = sol.isPossible(nums)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,2,3,3,4,5]
# output
output = sol.isPossible(nums)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]
# output
output = sol.isPossible(nums)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [2,2,3,3,3,4,4,4,5]
# output
output = sol.isPossible(nums)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,2,3,3,4,4,5,5]
# output
output = sol.isPossible(nums)
# answer
answer = True
print(output, answer, answer == output)

# input
nums = [1,2,3,4,4,5]
# output
output = sol.isPossible(nums)
# answer
answer = False
print(output, answer, answer == output)

# input
nums = [1,2,3,4,5,6]
# output
output = sol.isPossible(nums)
# answer
answer = True
print(output, answer, answer == output)
