from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = lambda x:tuple(sorted(x))
        group_anagram = defaultdict(list)
        for i in strs:
            group_anagram[anagram_map(i)].append(i)
        
        return_list = []
        for v in group_anagram.values():
            return_list.append(v)
        return return_list

sol = Solution()


# input
strs = ["eat","tea","tan","ate","nat","bat"]

# output
output = sol.groupAnagrams(strs)
# answer
answer = [["eat","tea","ate"],["tan","nat"],["bat"]]
print(output, answer, answer == output)

# input
strs = [""]

# output
output = sol.groupAnagrams(strs)
# answer
answer = [[""]]
print(output, answer, answer == output)

# input
strs = ["a"]

# output
output = sol.groupAnagrams(strs)
# answer
answer = [["a"]]
print(output, answer, answer == output)
