from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        s1_n = len(s1)
        s2_n = len(s2)
        s1_l = 0
        s2_l = 0
        s3_l = 0
        return_false = True
        while s1_l <s1_n or s2_l<s2_n:
            if s1[s1_l]==s3[s3_l] and s1_l<s1_n:
                return_false = False
                s1_l+=1
                s3_l+=1
            if s2[s2_l]==s3[s3_l] and s2_l<s2_n:
                return_false = False
                s2_l+=1
                s3_l+=1
            if return_false:
                return False
            return_false = True
        return True

sol = Solution()


# input
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
# output
output = sol.isInterleave(s1,s2,s3)
# answer
answer = True
print(output, answer, answer == output)

# input
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
# output
output = sol.isInterleave(s1,s2,s3)
# answer
answer = False
print(output, answer, answer == output)

# input
s1 = ""
s2 = ""
s3 = ""
# output
output = sol.isInterleave(s1,s2,s3)
# answer
answer = True
print(output, answer, answer == output)
