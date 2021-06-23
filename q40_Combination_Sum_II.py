from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result_list = []
        distinct_candidates_list = sorted(list(set(candidates)))
        def backtracking(nums, counter):
            if sum(nums)> target:
                return
            if sum(nums)== target:
                result_list.append(nums[:])
                return
            for candidate in distinct_candidates_list:
                if not nums or (nums and candidate>=nums[-1]):
                    if counter[candidate]:
                        counter[candidate]-=1
                        nums.append(candidate)
                        backtracking(nums,counter)
                        counter[candidate]+=1
                        nums.pop()
        backtracking([],Counter(candidates))
        return result_list
            

sol = Solution()


# input
candidates = [10,1,2,7,6,1,5]
target = 8
# output
output = sol.combinationSum2(candidates,target)
# answer
answer = [
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
print(output, answer, answer == output)

# input
candidates = [2,5,2,1,2]
target = 5
# output
output = sol.combinationSum2(candidates,target)
# answer
answer = [
[1,2,2],
[5]
]
print(output, answer, answer == output)
