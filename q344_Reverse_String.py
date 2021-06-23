from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            swap = s[i]
            s[i] = s[-i-1]
            s[-i-1] = swap


sol = Solution()

print(sol.reverseString())
