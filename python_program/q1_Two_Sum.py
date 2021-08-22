class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        range_array = range(len(nums))
        for i in range_array:
            for j in range_array[:i]+range_array[i+1:]:
                if nums[i]+nums[j]==target:
                    if i<j:
                        return (i,j)
                    else:
                        return (j,i)
        
