from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_counter = Counter(s)
        for c in t:
            if c in s_counter:
                s_counter[c]-=1
                if s_counter[c]==0:
                    del s_counter[c]
            else:
                return False
        return True

sol = Solution()


# input
s = "anagram"
t = "nagaram"
# output
output = sol.isAnagram(s,t)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "rat"
t = "car"
# output
output = sol.isAnagram(s,t)
# answer
answer = False
print(output, answer, answer == output)

# input
s = "rat"
t = "rarb"
# output
output = sol.isAnagram(s,t)
# answer
answer = False
print(output, answer, answer == output)
