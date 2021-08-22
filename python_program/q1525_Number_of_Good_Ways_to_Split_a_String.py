from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def numSplits(self, s: str) -> int:
        string_length = len(s)
        right_string_counter = Counter(s)
        left_string_counter = defaultdict(int)
        left_string_counter[s[0]] += 1
        right_string_counter[s[0]] -= 1
        if right_string_counter[s[0]] == 0:
            del right_string_counter[s[0]]
        
        good_split_count = 0
        for i in range(1,string_length-1):
            if len(left_string_counter)== len(right_string_counter):
                good_split_count += 1
            left_string_counter[s[i]] += 1
            right_string_counter[s[i]] -= 1
            if right_string_counter[s[i]] == 0:
                del right_string_counter[s[i]]
        if len(left_string_counter)== len(right_string_counter):
            good_split_count += 1
            
        return good_split_count

sol = Solution()

s = "aacaba"
print(sol.numSplits(s))

s = "abcd"
print(sol.numSplits(s))

s = "aaaaa"
print(sol.numSplits(s))

s = "acbadbaada"
print(sol.numSplits(s))
