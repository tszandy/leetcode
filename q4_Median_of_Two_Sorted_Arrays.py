from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        length_nums1 = len(nums1)
        length_nums2 = len(nums2)
        if length_nums1 == 0 and length_nums2 == 0:
            return 0
        if length_nums1 > length_nums2:
            return self.findMedianSortedArrays(nums2,nums1)
        low = 0
        high = length_nums1
        while (low <= high):
            middle_1 = (low+high)//2
            middle_2 = (length_nums1+length_nums2+1)//2-middle_1
            if middle_1 == 0:
                left_1 = float("-inf") 
            else: 
                left_1 = nums1[middle_1-1]
            
            if middle_2 == 0:
                left_2 = float("-inf") 
            else: 
                left_2 = nums2[middle_2-1]
            
            if middle_1 == length_nums1:
                right_1 = float("inf") 
            else: 
                right_1 = nums1[middle_1]
            
            if middle_2 == length_nums2:
                right_2 = float("inf") 
            else: 
                right_2 = nums2[middle_2]

            if left_1<= right_2 and left_2 <= right_1:
                if (length_nums1+length_nums2)%2==1:
                    return max(left_1,left_2)
                else:
                    return (max(left_1,left_2)+min(right_1,right_2))/2
            elif left_1 > right_2:
                high = middle_1-1
            elif left_2 > right_1:
                low = middle_1+1
        return 0
    


sol = Solution()


# input
nums1 = [1,3]
nums2 = [2]
# output
output = sol.findMedianSortedArrays(nums1,nums2)
# answer
answer = 2.00
print(output, answer, answer == output)

# input
nums1 = [1,2]
nums2 = [3,4]
# output
output = sol.findMedianSortedArrays(nums1,nums2)
# answer
answer = 2.500
print(output, answer, answer == output)

# input
nums1 = [0,0]
nums2 = [0,0]
# output
output = sol.findMedianSortedArrays(nums1,nums2)
# answer
answer = 0.00
print(output, answer, answer == output)

# input
nums1 = []
nums2 = [1]
# output
output = sol.findMedianSortedArrays(nums1,nums2)
# answer
answer = 1.00
print(output, answer, answer == output)

# input
nums1 = [2]
nums2 = []
# output
output = sol.findMedianSortedArrays(nums1,nums2)
# answer
answer = 2.00
print(output, answer, answer == output)

# input
nums1 = []
nums2 = [2,3]
# output
output = sol.findMedianSortedArrays(nums1,nums2)
# answer
answer = 2.5
print(output, answer, answer == output)
