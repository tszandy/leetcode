from collections import defaultdict
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        store =defaultdict(int)
        for i in nums:
            store[i]+=1
        for i in range(store[0]):
            nums[i]=0
        for i in range(store[0],store[0]+store[1]):
            nums[i]=1
        for i in range(store[0]+store[1],store[0]+store[1]+store[2]):
            nums[i]=2
        
