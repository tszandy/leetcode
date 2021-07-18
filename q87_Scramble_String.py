from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n == 1 and s1[0] == s2[0]:
            return True
        
        counter_left_to_right_s1 = Counter()
        counter_left_to_right_s2 = Counter()
        
        for i in range(n-1):
            counter_left_to_right_s1[s1[i]]+=1
            counter_left_to_right_s2[s2[i]]+=1
            if counter_left_to_right_s1 == counter_left_to_right_s2:
                if self.isScramble(s1[:i+1],s2[:i+1]) and self.isScramble(s1[i+1:],s2[i+1:]):
                    return True
        del counter_left_to_right_s1
        del counter_left_to_right_s2

        l = 0
        r = n-1
        counter_s1_left_to_right = Counter()
        counter_s2_right_to_left = Counter()
        
        for i in range(n-1):
            counter_s1_left_to_right[s1[l+i]]+=1
            counter_s2_right_to_left[s2[r-i]]+=1
            if counter_s1_left_to_right == counter_s2_right_to_left:
                if self.isScramble(s1[:i+1],s2[n-1-i:]) and self.isScramble(s1[i+1:],s2[:n-1-i]):
                    return True
        return False

sol = Solution()


# input
s1 = "a"

s2 = "b"

# output
output = sol.isScramble(s1,s2)
# answer
answer = False
print(output, answer, answer == output)

# input
s1 = "abcd"

s2 = "badc"

# output
output = sol.isScramble(s1,s2)
# answer
answer = True
print(output, answer, answer == output)

# input
s1 = "great"

s2 = "rgeat"

# output
output = sol.isScramble(s1,s2)
# answer
answer = True
print(output, answer, answer == output)

# input
s1 = "abcde"

s2 = "caebd"

# output
output = sol.isScramble(s1,s2)
# answer
answer = False
print(output, answer, answer == output)

# input
s1 = "a"

s2 = "a"

# output
output = sol.isScramble(s1,s2)
# answer
answer = True
print(output, answer, answer == output)

# input
s1 = "abcdbdacbdac"

s2 = "bdacabcdbdac"

# output
output = sol.isScramble(s1,s2)
# answer
answer = True
print(output, answer, answer == output)

# input
s1 = "oatzzffqpnwcxhejzjsnpmkmzngneo"

s2 = "acegneonzmkmpnsjzjhxwnpqffzzto"

# output
output = sol.isScramble(s1,s2)
# answer
answer = True
print(output, answer, answer == output)
