from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            iter_length = min(len(string),len(prefix))
            for i in range(iter_length):
                if prefix[i]!=string[i]:
                    prefix = prefix[:i]
                    break
            if len(string) < len(prefix):
                prefix = string
        return prefix    

sol = Solution()

strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(sol.longestCommonPrefix(strs))

strs = ["ab", "a"]
print(sol.longestCommonPrefix(strs))

