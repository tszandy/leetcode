from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        max_difference = 1
        count_difference = 1
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])<=difference:
                count_difference+=1
            elif max_difference <count_difference:
                max_difference = count_difference
                count_difference = 1
        if max_difference <count_difference:
            max_difference = count_difference
        return max_difference
                
        

sol = Solution()

print(sol.longestSubsequence())