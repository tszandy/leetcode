from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)==1:
            return False
        nums = list(map(lambda x:x%k,nums))
        subarray_sum = [(nums[0],(0,0))]
        for i in range(1,len(nums)):
            new_subarray_sum = []
            for subsum in subarray_sum:
                value, index = subsum
                if (value+nums[i]) % k ==0:
                    return True
                new_subarray_sum.append((value+nums[i],(index[0],i)))
                
                if nums[i]==0 and index[1]-index[0]>=1:
                    new_subarray_sum.append((value-nums[index[0]],(index[0]+1,i)))
                index_left = index[0]
                while (value+nums[i])//k>value//k:
                    if (value+nums[i])%k==0:
                        return True
                    value -= nums[index_left]
                    index_left+=1
                if index_left != index[0]:
                    new_subarray_sum.append((value+nums[i],(index_left,i)))
            subarray_sum = new_subarray_sum
        for subsum in subarray_sum:
            value, index = subsum
            if value+nums[i] % k ==0:
                return True
        return False            
            

sol = Solution()

print(sol.checkSubarraySum())