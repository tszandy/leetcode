from typing import List

import numpy as np

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_to_right_cumsum = np.cumsum(nums)
        right_to_left_cumsum = np.cumsum(nums[::-1])[::-1]
        
        result_list = []
        length_nums = len(nums)
        result_list.append(right_to_left_cumsum[0]-nums[0]*(length_nums))
        for i in range(1,length_nums-1):
            greater_count = i+1
            less_count = i-1
            greater_count_sum = right_to_left_cumsum[greater_count]-nums[i]*(length_nums-greater_count+1)
            less_count_sum = -left_to_right_cumsum[less_count]+nums[i]*(i+1)
            
            result_list.append(greater_count_sum+less_count_sum)
        result_list.append(-left_to_right_cumsum[-1]+nums[-1]*(length_nums))
        return result_list

sol = Solution()

print(sol.getSumAbsoluteDifferences())