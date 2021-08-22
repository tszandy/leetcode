from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num]+=1
        reachable = defaultdict(list)
        self_reachable = defaultdict(bool)
        distinct_nums = list(nums_count.keys())
        for i in range(len(distinct_nums)):
            self_reachable[distinct_nums[i]] = self.sum_is_something_square(distinct_nums[i],distinct_nums[i])
            for j in range(i+1,len(distinct_nums)):
                if self.sum_is_something_square(distinct_nums[i],distinct_nums[j]):
                    reachable[distinct_nums[i]].append(distinct_nums[j])
                    reachable[distinct_nums[j]].append(distinct_nums[i])
                
                
    def sum_is_something_square(self, a: int, b:int) -> bool:
        return math.floor(math.sqrt(a+b))**2==a+b
        

sol = Solution()

print(sol.numSquarefulPerms())