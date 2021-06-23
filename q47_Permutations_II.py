from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        num_counter = Counter(nums)
        
        list_distinct_nums = sorted(list(num_counter.keys()))
        next_state_dict = dict(zip(list_distinct_nums[:-1],list_distinct_nums[1:]))
        
        result_list = []
        
        def backtracking(construct_list, counter):
            if len(construct_list) == nums_length:
                result_list.append(construct_list[:])
                return
            
            num = list_distinct_nums[0]
            while num in next_state_dict:
                if num_counter[num] > 0:
                    construct_list.append(num)
                    counter[num]-=1
                    
                    backtracking(construct_list,counter)
                    construct_list.pop()
                    counter[num]+=1
                num = next_state_dict[num]
            else:
                if num_counter[num] > 0:
                    construct_list.append(num)
                    counter[num]-=1

                    backtracking(construct_list,counter)
                    construct_list.pop()
                    counter[num]+=1
        backtracking([],num_counter)
        
        return result_list

sol = Solution()

nums = [1,1,2]
print(sol.permuteUnique(nums))

nums = [1,2,3]
print(sol.permuteUnique(nums))
