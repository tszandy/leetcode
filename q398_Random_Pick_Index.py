import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.store_nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        return_index = -1
        for i,num in enumerate(self.store_nums):
            if target==num:
                count+=1
                if random.random()<=1.0/count:
                    return_index=i
        return return_index


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
