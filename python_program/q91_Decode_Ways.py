from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if len(s)==0:
            return 1
        if s[0]=="0":
            return 0
        if len(s)==1:
            return 1
        if s[0]=="1":
            return self.numDecodings(s[1:])+self.numDecodings(s[2:])
        if s[0]=="2":
            if int(s[1])<=6:
                return self.numDecodings(s[1:])+self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:])
        if int(s[0])>2:
            return self.numDecodings(s[1:])

sol = Solution()


# input
s = "12"

# output
output = sol.numDecodings(s)
# answer
answer = 2
print(output, answer, answer == output)

# input
s = "226"

# output
output = sol.numDecodings(s)
# answer
answer = 3
print(output, answer, answer == output)

# input
s = "0"

# output
output = sol.numDecodings(s)
# answer
answer = 0
print(output, answer, answer == output)

# input
s = "06"

# output
output = sol.numDecodings(s)
# answer
answer = 0
print(output, answer, answer == output)

# input
s = "2220620626222662266226222626226226247892174895198260622222222666622606"

# output
output = sol.numDecodings(s)
# answer
answer = 0
print(output, answer, answer == output)

# input
s = "22206206262226622662262226262262262478921748951982662222222266662266"

# output
output = sol.numDecodings(s)
# answer
answer = 64152000
print(output, answer, answer == output)
